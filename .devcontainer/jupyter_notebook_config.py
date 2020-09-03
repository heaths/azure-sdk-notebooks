# Copyright 2020 Heath Stewart.
# Licensed under the MIT License. See LICENSE.txt in the project root for license information.

import os

c.NotebookApp.notebook_dir = '/home/{}/work'.format(os.environ['NB_USER'])
c.NotebookApp.open_browser = False
c.NotebookApp.quit_button = False
