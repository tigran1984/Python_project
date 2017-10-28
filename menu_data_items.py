#main_dict = {}
#dict22 = { 1 : 'Func_name',
#          2 :[ File , New ],
#          3 : "Icon_Image",
#          4 : "Shortcut_Key",
#          5 : "Tool_Description",
#          6 : "Menu_Location" }
#
#dict1 = { 1 : 'Func_name',
#          2 : "Tool_Name",
#          3 : "Icon_Image",
#          4 : "Shortcut_Key",
#          5 : "Tool_Description",
#          6 : "Menu_Location" }
main_dict  = {   }


my_dict0 =  {
           1 : 'load_image',
           2 : 'Load  Image',
           3 : '/home/tiko/Image_Editor_Qt_19.02.2016/importimg.png',
           4 : 'Alt+I',
           5 : 'Importing selected Image',
           6 : 'File'}
main_dict.update( {0 : my_dict0} )
my_dict1 =  {
           1 : 'save_image',
           2 : 'Save Image',
           3 : '/home/tiko/Image_Editor_Qt_19.02.2016/saveimg.png',
           4 : 'Alt+Shift+S',
           5 : 'Saveing image',
           6 : 'File'}

main_dict.update( {1 : my_dict1} )
my_dict2 =  {
           1 : 'blur_picture',
           2 : 'Blur',
           3 : '',
           4 : 'Alt+B',
           5 : 'Image Bluring Effect',
           6 : 'Options'}
main_dict.update( {2 : my_dict2} )
my_dict3 =  {
           1 : 'sharpen_picture',
           2 : 'Sharpen',
           3 : '',
           4 : 'Alt+S',
           5 : 'Sharpening Image',
           6 : 'Options'}
main_dict.update( {3 : my_dict3} )
