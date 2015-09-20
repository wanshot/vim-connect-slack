vim-connect-slack
====================
vim-connect-slack will run the SlackAPI from Vim

This Plugin is still BetaVersion

Requirements
=================
* Vim == +python/dyn
  * Python >= 2.7.9
  * requests
    
       or
    
   * Python < 2.7.9
   * requests <= 2.5.3   



Settings
=================
Plz set these to vimrc

    let g:Token = "Your Slack Token"
    let g:UserName = "Your Slack Username"
    let g:Channnel = "Default Channel ID"
    # Channel you can be set in the command
    
    

Commands
=================

* POST Message

  `:Slack "Message"`

* POST Snippet
   
  Range selection change to the visual mode  
  
  `:SlackSnippet {FileType} {Title}`
  * Default FileType is "Python"
  * Default Title is "None"

* Show Channel History

  `:SlackHistory {Count}`
  * Count is int
 

* Show SlackChannels

  `:SlackChannels`


* Show Current channel

  `:SlackChannel`


* Set Channel

   `:SlackChannels`  
   * Enter button to select the channel list that is displayed



License
=================
This software is released under the MIT License, see LICENSE.txt.
