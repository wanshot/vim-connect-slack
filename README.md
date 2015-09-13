vim-connect-slack
====================
vim-connect-slack will run the SlackAPI form Vim

This Plugin is still BetaVersion

Requirements
=================
* Python >= 2.7.9
* requests

  or

* Python < 2.7.9
* requests <= 2.5.3   



Example .vimrc
=================
Setting your vimrc

    let g:Token = "Your Slack Token"   
    let g:Channnel = "Target Channel"
    let g:UserName = "Your Slack Username"


Commands
=================

* POST Message

  `:Slack "Message"`

* POST Snippet
   
  Range selection change to the visual mode  
  
  `:SlackSnippet {FileType} {Title}`
  * Default FileType is "Python"
  * Default Title is "None"
   
* Show SlackChannels

  `:SlackChannel`

* Change Channel

   `:let Channel = "Target Channel ID"`




License
=================
This software is released under the MIT License, see LICENSE.txt.