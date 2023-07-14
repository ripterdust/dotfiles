" Configuraciones generales
set number
set mouse=a
syntax enable
set showcmd
set sw=2
set encoding=utf-8
set showmatch

call plug#begin('~/.config/nvim/plugins')
"Tema
Plug 'sainnhe/gruvbox-material'

"LSP
Plug 'neovim/nvim-lspconfig'

call plug#end()

" GRUVBOX configuración
set background=dark
let g:gruvbox_material_background='medium'
colorscheme gruvbox-material

"LSP configuración

