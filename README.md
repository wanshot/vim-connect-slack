vim-connect-slack
====================
-----------------------------------------------
vim-connect-slack will run the SlackAPI form Vim

This Plugin is still BetaVersion

Requirements
=================
-----------------------------------------------
* Python >= 2.7.9
* requests

  or

* Python < 2.7.9
* requests >= 2.5.3   



Example .vimrc
=================
------------------------------------------------
setting your vimrc


    let g:token = "Your Slack Token"   
    let g:channnel = "Target Channel"
    let g:username = "Your Slack Username"


Commands
=================
------------------------------------------------

* POST Message

  `:Slack "Message"`

* POST Snippet

  `:SlackSnippet {FileType} {Title}`
  * Default FileType is  "Python"
  * Default Title is "None"
   
* Show SlackChannels

  `:SlackChannel`




License
=================
------------------------------------------------
This software is released under the MIT License, see LICENSE.txt.




 