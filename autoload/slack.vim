" version: 0.9.4
" author : wan <one_kkm@icloud.com>
" license: mit license

let s:save_cpo = &cpo
set cpo&vim

let s:script_dir = expand('<sfile>:p:h')

function! s:Selection() range
    let tmp = @@
    silent normal gvy
    let selected = @@
    let @@ = tmp
    return selected
endfunction

function! s:Slack_info() abort
    if !exists('g:Token')
        return "Plz set the Token"
    elseif !exists('g:Channel')
        return "Plz set The Channel"
    elseif !exists('g:UserName')
        return "Plz set the UserName"
    endif
    return {'token': g:Token, 'channel': g:Channel, 'username': g:UserName}
endfunction

function! s:Slack_info_token() abort
    if !exists('g:Token')
        return "Plz set the Token"
    endif
    return {'token': g:Token}
endfunction


pyfile <sfile>:h:h/slack.py
python import vim

function! slack#channels()
  python show_channels(vim.eval('s:Slack_info_token()'))
endfunction

function! slack#channel()
    python get_channel_name(vim.eval('s:Slack_info()'))
endfunction

function! slack#history(args)
  python show_history(vim.eval('s:Slack_info()'), vim.eval('a:args'), vim.eval('s:script_dir'))
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

function! RenderSlackChannelsBuffer()
    exe "new __SlackChannels__"
    nnoremap <script> <silent> <buffer> <Enter> :call <sid>ChoiceChannel()<CR>
    nnoremap <script> <silent> <buffer> q             :call <sid>SlackChannelsClose()<CR>
    cabbrev  <script> <silent> <buffer> q             call <sid>SlackChannelsClose()
endfunction


function! s:ChoiceChannel()
    let target_line = getline('.')
    if exists("g:Channel")
        unlet! g:Channel
        python choice_channel(vim.eval('s:Slack_info_token()'), vim.eval('target_line'), vim.eval('s:script_dir'))
        call s:SlackChannelsClose()
   endif
        python choice_channel(vim.eval('s:Slack_info_token()'), vim.eval('target_line'), vim.eval('s:script_dir'))
        call s:SlackChannelsClose()
endfunction

function! s:SlackChannelsBufferName(name)
    if bufwinnr(bufnr(a:name)) != -1
        exe bufwinnr(bufnr(a:name)) . "wincmd w"
        return 1
    else
        return 0
    endif
endfunction

function! s:SlackChannelsClose()
    if s:SlackChannelsBufferName('__SlackChannels__')
        quit
        let deletefile = '__SlackChannels__'
        call delete(deletefile)
    endif
endfunction

function! slack#mode_change()
    python Database().mode_on(vim.eval('s:script_dir'), vim.eval('s:Slack_info_token()'))
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo 
