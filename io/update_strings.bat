set root_dir=%1
set target_dir=%2

python .\file_rename.py -o "Resources.resw" -n "DiscussionEditFormResources.resw" -d %root_dir%\BbCourseDiscussionEditForm
python .\file_rename.py -o "Resources.resw" -n "DiscussionGroupResources.resw" -d %root_dir%\BbCourseDiscussionGroup
python .\file_rename.py -o "Resources.resw" -n "DiscussionThreadResources.resw" -d %root_dir%\BbCourseDiscussionThread


python update_strings.py -s %root_dir% -t %target_dir%