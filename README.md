# Internet Archive Uploader
 This project is a simple wrapper for file/directory uploads built around the [Internet Archive](https://archive.org/developers/internetarchive/) library. To use it you must have an existing account on the Internet Archive.

# Usage
To install the library
```
pip install internet-archive-uploader
```
To use the library

```python
from InternetArchiveUploader import InternetArchiveUploader

uploader= InternetArchiveUploader(
  'myUniqueIdentifier',
  {'metadataAttribute1':'something'},
  'Your Internet Archive username/email',
  'Your Internet Archive password',
)

uploader.uploadFile('/path/to/file')

uploader.uploadDirectory('/path/to/directory')
```

The identifier must be unique for internet archive to create the archive but after that you can repeatedly use it to upload more files to that collection.

The metadata is a dictionary of metadata attributes with their values. You can learn more about [metadata](https://archive.org/developers/metadata-schema/index.html) here.

The password and username should be self explanatory.

# Contributions
If anyone uses this library and has issues or wants to contribute feel free to message me. I am willing to add extra features or do bug fixes. It should also be noted that I am using this package primarily to distribute my code for personal use and gain experience in publishing python packages.
