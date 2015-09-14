" version: 0.9.1
" author : wan <one_kkm@icloud.com>
" license: mit license

if exists("g:loaded_slack")
  finish
endif
let g:loaded_slack = 1
let s:save_cpo = &cpo
set cpo&vim

command! SlackChannel call slack#channel()
command! SlackChannels call slack#channels()
command! -nargs=1 Slack call slack#slack(<f-args>)
command! -nargs=+ SlackSnippet call slack#snippet(<f-args>)
command! -nargs=1 SlackHistory call slack#history(<f-args>)

let &cpo = s:save_cpo
unlet s:save_cpo
