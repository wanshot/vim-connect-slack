" version: 0.9.0
" author : wan <one_kkm@icloud.com>
" license: mit license

let s:save_cpo = &cpo
set cpo&vim

function! s:Selection() range
    let tmp = @@
    silent normal gvy
    let selected = @@
    let @@ = tmp
    return selected
endfunction

function! s:Slack_info()
    return {'token': g:Token, 'channel': g:Channel, 'username': g:UserName}
endfunction


pyfile <sfile>:h:h/slack.py
python import vim

function! slack#channel()
  python show_channels(vim.eval('s:Slack_info()'))
endfunction
 
function! slack#slack(args)
  python post(vim.eval('s:Slack_info()'), vim.eval('a:args'))
endfunction

function! slack#snippet(args, ...)
    let title = get(a:, 1, 'None')
    let a:Args =  [a:args, title]
    call s:Action_snippet(a:Args)
endfunction

function! s:Action_snippet(args)
    python post_snippet(vim.eval('s:Slack_info()'), vim.eval('s:Selection()'), vim.eval('a:args'))
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo 
