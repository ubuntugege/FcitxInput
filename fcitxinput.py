import sublime, sublime_plugin
import os, sys, stat, shutil, subprocess, zipfile

st_platform = sublime.platform()
st_arch = sublime.arch()
st_version = sublime.version()
st_ver = st_version[0]

if st_ver == "2":
	reload(sys)
	sys.setdefaultencoding('utf-8')

pkg_dir = os.path.dirname(os.path.abspath(__file__))
pkg_name = os.path.basename(pkg_dir)
if '.' in pkg_name:
	pkg_name = pkg_name.split('.')[0]

class FcitxinputCommand(sublime_plugin.ApplicationCommand):
	def run(self, build_version):
		run_create(build_version)

class SfInstructionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		view.set_name("FcitxInput")
		view.settings().set("word_wrap", True)
		instruction_dir = os.path.join(pkg_dir, "locale", "instruction");
		instruction = os.path.join(instruction_dir, "instruction.txt")
		locale_instruction = os.path.join(instruction_dir, "instruction."+locale+".txt")
		if os.path.isfile(locale_instruction):
			instruction = locale_instruction
		view.insert(edit, 0, file_get_contents(instruction))
		view.set_scratch(True)
		view.set_read_only(True)

def run_create(build_version = False):
	if st_platform != "linux":
		sublime.error_message(pkg_name+" only needed on linux platform.")
		return

	st_exe = get_exe()
	if st_ver == "2" and not os.path.isfile(st_exe):
		sublime.active_window().new_file().run_command("sf_instruction")
		return

	fcitx_ver = check_output("fcitx --version")
	fcitx_ver = fcitx_ver.strip().decode("utf-8")
	if fcitx_ver.find("fcitx version: ") == -1:
		sublime.active_window().new_file().run_command("sf_instruction")
		return

	if build_version:
		version = st_version
	else:
		version = st_ver
	make_launch_shell(version)
	create_desktop_entry(version)
	sublime.status_message("Create Desktop Entry for Sublime Text "+version+" Done.")

def make_launch_shell(version):
	st_exe = get_exe()
	shell = file_get_contents(os.path.join(pkg_dir, ".sublime_fcitx.sh"))
	shell = shell.replace("{st_exe}", st_exe)
	shell = shell.replace("{pkg_dir}", pkg_dir)
	shell = shell.replace("{arch}", st_arch)

	st_sh_v = os.path.join(pkg_dir, "sublime_text_fcitx.sh")
	st_sh_b = os.path.join(pkg_dir, "sublime_text_"+version+"_fcitx.sh")

	file_put_contents(st_sh_v, shell.replace("{version}", ""))
	file_put_contents(st_sh_b, shell.replace("{version}", "_"+version))

	os.chmod(st_sh_v, os.stat(st_sh_v).st_mode | stat.S_IEXEC)
	os.chmod(st_sh_b, os.stat(st_sh_b).st_mode | stat.S_IEXEC)

	bin_dir = os.path.expanduser("~")+"/.local/bin"
	if not os.path.isdir(bin_dir):
		os.makedirs(bin_dir)

	st_bin_v = os.path.join(bin_dir, "sublime_text_fcitx")
	st_bin_b = os.path.join(bin_dir, "sublime_text_"+version+"_fcitx")
	shutil.copyfile(st_sh_v, st_bin_v)
	shutil.move(st_sh_b, st_bin_b)
	os.chmod(st_bin_v, os.stat(st_bin_v).st_mode | stat.S_IEXEC)

def create_desktop_entry(version):
	st_dir = get_dir()
	st_icon = "sublime-text"
	if st_ver == "2":
		st_icon = st_icon+"-"+st_ver

	shortcut = file_get_contents(os.path.join(pkg_dir, ".sublime_fcitx.desktop"))
	shortcut = shortcut.replace("{pkg_dir}", pkg_dir)
	shortcut = shortcut.replace("{st_icon}", st_icon)

	st_v_shortcut = os.path.join(pkg_dir, "sublime_text_fcitx.desktop")
	st_b_shortcut = os.path.join(pkg_dir, "sublime_text_"+version+"_fcitx.desktop")

	file_put_contents(st_v_shortcut, shortcut.replace("{version}", ""))
	file_put_contents(st_b_shortcut, shortcut.replace("{version}", " "+version))

	app_dir = os.path.expanduser("~")+"/.local/share/applications"
	if not os.path.isdir(app_dir):
		os.makedirs(app_dir)

	app_v_shortcut = os.path.join(app_dir, "sublime_text_fcitx.desktop")
	app_b_shortcut = os.path.join(app_dir, "sublime_text_"+version+"_fcitx.desktop")
	shutil.copyfile(st_v_shortcut, app_v_shortcut)
	shutil.copyfile(st_b_shortcut, app_b_shortcut)

	icon_size_list = ["16", "32", "48", "128", "256"]
	if st_ver == "2":
		for size in icon_size_list:
			icon_file = os.path.join(st_dir, "Icon/"+size+"x"+size+"/sublime_text.png")
			# check_output("xdg-icon-resource install --size "+size+" '"+icon_file+"' sublime-text-2")
			icon_target = os.path.expanduser("~")+"/.local/share/icons/hicolor/"+size+"x"+size+"/apps/sublime-text-2.png"
			icon_dir = os.path.dirname(icon_target)
			if not os.path.isdir(icon_dir):
				os.makedirs(icon_dir)
			shutil.copyfile(icon_file, icon_target)
		desktop_dir = check_output("xdg-user-dir DESKTOP")
	else:
		for size in icon_size_list:
			icon_file = os.path.join(st_dir, "Icon/"+size+"x"+size+"/sublime-text.png")
			subprocess.check_output(["xdg-icon-resource", "install", "--size", size, icon_file, "sublime-text"])
		desktop_dir = subprocess.check_output(["xdg-user-dir", "DESKTOP"])
	desktop_dir = desktop_dir.strip().decode("utf-8")

	desktop_v_shortcut = os.path.join(desktop_dir, "sublime_text_fcitx.desktop")
	desktop_b_shortcut = os.path.join(desktop_dir, "sublime_text_"+version+"_fcitx.desktop")
	shutil.copyfile(st_v_shortcut, desktop_v_shortcut)
	shutil.move(st_b_shortcut, desktop_b_shortcut)

	os.chmod(st_v_shortcut, os.stat(st_v_shortcut).st_mode | stat.S_IEXEC)
	os.chmod(app_v_shortcut, os.stat(app_v_shortcut).st_mode | stat.S_IEXEC)
	os.chmod(app_b_shortcut, os.stat(app_b_shortcut).st_mode | stat.S_IEXEC)
	os.chmod(desktop_v_shortcut, os.stat(desktop_v_shortcut).st_mode | stat.S_IEXEC)
	os.chmod(desktop_b_shortcut, os.stat(desktop_b_shortcut).st_mode | stat.S_IEXEC)

def get_exe():
	if st_ver == "2":
		st_exe = sublime.load_settings(pkg_name+".sublime-settings").get("st_exe", "")
	else:
		st_exe = sublime.executable_path()
	return st_exe

def get_dir():
	st_dir = os.path.dirname(get_exe())
	return st_dir

def check_output(cmd):
	process_list = []
	cmd_list = cmd.strip().split("|")
	for i, sub_cmd in enumerate(cmd_list):
		cmd_list = sub_cmd.strip().split(" ")
		STDIN = None
		if i > 0:
			STDIN = process_list[i - 1].stdout
		process_list.append(subprocess.Popen(cmd_list, stdin=STDIN, stdout=subprocess.PIPE))
	if len(process_list) == 0:
		return ""
	output = process_list[i].communicate()[0]
	return output

def update_tool_menu():
	origin_menu = os.path.join(pkg_dir, ".menu.json")
	locale_menu = os.path.join(pkg_dir, "locale", "menu", locale+".json")
	if os.path.isfile(locale_menu):
		menu = file_get_contents(locale_menu)
	else:
		menu = file_get_contents(origin_menu)
	file_put_contents(os.path.join(pkg_dir, "Main.sublime-menu"), menu)

def update_command_menu():
	origin_menu = os.path.join(pkg_dir, ".command.json")
	locale_menu = os.path.join(pkg_dir, "locale", "command", locale+".json")
	if os.path.isfile(locale_menu):
		menu = file_get_contents(locale_menu)
	else:
		menu = file_get_contents(origin_menu)
	file_put_contents(os.path.join(pkg_dir, pkg_name+".sublime-commands"), menu)

def update_menu():
	global locale
	locale = sublime.load_settings(pkg_name+".sublime-settings").get("locale", "en_US")
	update_tool_menu()
	update_command_menu()

def file_get_contents(filename):
	with open(filename, "r") as f:
		return f.read()

def file_put_contents(filename, content):
	with open(filename, "w") as f:
		return f.write(content)

def unpack(filename, to_dir):
	z = zipfile.ZipFile(filename, 'r')
	files = [i.filename for i in z.infolist()]
	for item in files:
		z.extract(item, to_dir)
	z.close()

def plugin_loaded():
	sublime.set_timeout(init, 200)

def init():
	if st_platform != "linux":
		return
	if st_ver == '3' and os.path.isfile(pkg_dir):
		to_dir = os.path.join(sublime.packages_path(), pkg_name);
		if not os.path.isdir(to_dir):
			unpack(pkg_dir, to_dir)
		return
	update_menu()
	sublime.load_settings(pkg_name+".sublime-settings").add_on_change('locale', update_menu)
	sublime.load_settings(pkg_name+".sublime-settings").add_on_change('st_exe', run_create)

if (st_ver == "2"):
	init()
