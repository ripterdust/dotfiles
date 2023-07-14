require('nvim-treesitter.configs').setup{
  ensure_installed = {"python", "css", "lua", "html", "typescript", "java"},
  sync_install = false,
  auto_install = true,
  highlight = {
	  enable = true
  }	
}
