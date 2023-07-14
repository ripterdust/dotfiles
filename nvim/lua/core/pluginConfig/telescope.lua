local builtin = require('telescope.builtin')

vim.keymap.set('n', 'p', builtin.find_files, {})
