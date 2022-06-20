"setting number
set number

set nocompatible

" setting terminal colors
set termguicolors
syntax enable
let g:Hexokinase_highlighters = ['backgroundfull']
let g:Hexokinase_optInPatterns = 'full_hex,rgb,rgba,hsl,hsla,colour_names'
call plug#begin("~/vim/plugged")
" vim colors shower
Plug 'rrethy/vim-hexokinase', { 'do': 'make hexokinase' }
" theme 
Plug 'chriskempson/base16-vim'
"file manager
Plug 'preservim/nerdtree'
Plug 'sonph/onehalf', { 'rtp': 'vim' }
Plug 'morhetz/gruvbox'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()

colorscheme base16-tomorrow-night 
