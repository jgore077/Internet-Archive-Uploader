Remove-Item 'dist' -Confirm:$false -Recurse
Remove-Item 'internet_archive_uploader.egg-info' -Confirm:$false -Recurse
pip install -e . 
py -m build