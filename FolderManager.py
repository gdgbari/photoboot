import os

import yaml

import utils

from SettingsManager import Settings

# FOLDERS EXPLANATION
#
#    main_folder
#       |___________> current       [ here the current shots: in future the user would choose from different shots]
#       |___________> originals     [ all the originals chosen shots                                              ]
#       |___________> output        [ all the outputs: cropped and cornered                                       ]
#

class FolderManager:

    def __init__(self, main_folder_path: str):

        self._main_folder_path = main_folder_path
        # now the paths of all the sub-folders
        self._current_folder_path = os.path.join(main_folder_path,'current')
        self._originals_folder_path = os.path.join(main_folder_path,'originals')
        self._output_folder_path = os.path.join(main_folder_path,'output')

        # then we check the folders consistency
        self._folder_consistency_assurance()

    def _folder_consistency_assurance(self):
        # if the sub-folders misses, will be created
        folder_list = [self._main_folder_path, self._current_folder_path,
                       self._originals_folder_path, self._output_folder_path]
        for folder in folder_list:
            if not os.path.exists(folder):
                os.makedirs(folder)
                os.chmod(folder, 0o777)

    def get_current_path(self) -> str:
        return self._current_folder_path

    def get_originals_path(self) -> str:
        return self._originals_folder_path

    def get_output_folder_path(self) -> str:
        return self._output_folder_path

class FileNaming:

    def __init__(self):
        self._temp_data_path = "./temp_data.yaml"
        self._settings = Settings()

    def get_photo_name(self) -> str:
        with open(self._temp_data_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)

        session_number = yaml_dict["session"]

        folder = FolderManager(self._settings.get_main_folder_path())
        photo_number = utils.get_string_from_photo_number(len(os.listdir(folder.get_current_path())) + 1)

        return f"DEVFESTBA_{utils.get_string_from_session_number(int(session_number) + 1)}_{photo_number}.jpg"

    def get_session_number(self) -> str:
        with open(self._temp_data_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)

        session_number = yaml_dict["session"]

        return utils.get_string_from_session_number(int(session_number) + 1)
