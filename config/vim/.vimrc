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

call plug#end()

colorscheme base16-tomorrow-night
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
