    def runProgramInOtherThread(self):
        time.sleep(20)
        filePickerFile = ft.file_picker.FilePickerFile("1accounts 2.json", "/Volumes/Macintosh HD/Users/mostafajalalhoseiny/Downloads/temp projects/1402/Python/1accounts 2.json", os.path.getsize("/Volumes/Macintosh HD/Users/mostafajalalhoseiny/Downloads/temp projects/1402/Python/1accounts 2.json"))
        self.home_page.pick_accounts_result(ft.FilePickerResultEvent(None, filePickerFile))
        self.home_page.start(None)
