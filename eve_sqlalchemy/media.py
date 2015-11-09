# -*- coding: utf-8 -*-
"""
 
 Media storage for sqlalchemy extenstion.
 
 :copyright: (c) 2014 by Andrew Mleczko
 :license: BSD, see LICENSE for more details.
 
"""
from __future__ import unicode_literals

from io import BytesIO

import base64
import mimetypes

from io import BytesIO

from eve.io.media import MediaStorage


class SQLBlobMediaStorage(MediaStorage):
    """
    The MediaStorage class provides a standardized API for storing files,
    along with a set of default behaviors that all other storage systems can
    inherit or override as necessary.
    
    ..versioneadded:: 0.3
    """
    
    def get(self, content, resource=None):
        """
        Opens the file given by name or unique id. Note that although the
        returned file is guaranteed to be a File object, it might actually be
        some subclass. Returns None if no file was found.
        """
        
        byte_stream = BytesIO(content)
        
        # Monkey patch EXTENDED_MEDIA_INFO attributes onto the byte stream object..
        #byte_stream.content_type = mimetypes.guess_type(filename)[0]
        byte_stream.content_type = "text/plain"
        #byte_stream.name = filename
        byte_stream.name = "filename.ext"
        byte_stream.length = len(content)
        
        return byte_stream
    
    def put(self, content, filename=None, content_type=None, resource=None):
        """
        Saves a new file using the storage system, preferably with the name
        specified. If there already exists a file with this name name, the
        storage system may modify the filename as necessary to get a unique
        name. Depending on the storage system, a unique id or the actual name
        of the stored file will be returned. The content type argument is used
        to appropriately identify the file when it is retrieved.
        """
        content.stream.seek(0)
        return content.stream.read()
    
    def delete(self, id_or_filename, resource=None):
        """
        Deletes the file referenced by name or unique id. If deletion is
        not supported on the target storage system this will raise
        NotImplementedError instead
        """
        if not id_or_filename:  # there is nothing to remove
            return
    
    def exists(self, id_or_filename, resource=None):
        """
        Returns True if a file referenced by the given name or unique id
        already exists in the storage system, or False if the name is available
        for a new file.
        """
        raise NotImplementedError
