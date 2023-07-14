require("bufferline").setup{
options = {
    mode = "buffers",
    numbers = "ordinal",
    indicator = {
      style = 'icon'
     },
   hover = {
     enabled = true,
     reveal = {'close'},
     delay= 200
     },
    left_mouse_comman = 'buffer %d',
    right_mouse_command = 'buffer delete',
    buffer_close_icon = 'X',
    diagnostics = 'coc',
    show_close_icon = true,
    
  }
}
