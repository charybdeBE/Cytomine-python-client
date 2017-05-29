# -*- coding: utf-8 -*-


#
# * Copyright (c) 2009-2017. Authors: see NOTICE file.
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *      http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# */

__author__          = "Laurent Vanosmael " 
__contributors__    = []                
__copyright__       = "Copyright 2010-2017 University of Liège, Belgium, http://www.cytomine.be/"


from model import Model
from collection import Collection


class ImageGroupHDF5(Model):

    def __init__(self, params = None):
        super(ImageGroupHDF5, self).__init__(params)
        self._callback_identifier = "imagegrouphdf5"

    def to_url(self):
        if hasattr(self, "group"):
            return "imagegroup/%d/imagegrouph5.json" % self.group
	elif hasattr(self, "id"):
            return "imagegrouphdf5/%d.json" % self.id
        else:
            return "imagegrouphdf5.json"

    def __str__( self ):
        return "%s : %s " % (self.id, self.filenames)

class ImageGroupSpectra(Model):
    def __init__(self, params = None):
        super(ImageGroupSpectra, self).__init__(params)
        self._callback_identifier = "imagegroupspectra"

    def to_url(self):
        return "imagegroup/%d/%d/%d/pxl.json" % (self.id, self.x, self.y)

    def __str__( self ):
        return "%s : %s " % (self.position, self.spectra)


class ImageSequence(Model):
    def __init__(self, params = None):
        super(ImageSequence, self).__init__(params)
        self._callback_identifier = "imagesequence"

    def to_url(self):
        if hasattr(self, "id"):
            return "imagesequence/%d.json" % self.id
        else:
            return "imagesequence.json"

    def __str__( self ):
        return "%s " % (self.id)


class ImageSequenceCollection(Collection):    
    def __init__(self, params = None):
        super(ImageSequenceCollection, self).__init__(ImageSequence, params)

    def to_url(self):
        if hasattr(self, "group"):
            return "imagegroup/%d/imageinstance.json"
        else:
            return "imagesequence.json"



