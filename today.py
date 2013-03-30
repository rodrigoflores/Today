import sublime, sublime_plugin, time;

class TodayCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for cursor in self.view.sel():
      self.view.insert(edit, cursor.begin(), time.strftime("%d/%m/%Y"));