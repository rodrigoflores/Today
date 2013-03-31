import sublime, sublime_plugin, time;

settings = sublime.load_settings('Today.sublime-settings')

class TodayCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    format = settings.get('date_format');
    for cursor in self.view.sel():
      self.view.insert(edit, cursor.begin(), time.strftime(format));

class NowCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    format = settings.get('time_format');
    for cursor in self.view.sel():
      self.view.insert(edit, cursor.begin(), time.strftime(format));