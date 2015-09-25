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
    
    

Usage
=================

Please be the first to run the SlackMode To use the vim-connect-slack

    :SlackMode
  
  SlackMode caches the information of API inside
  
  When information of the slack has been updated please run the SlackMode


Commands
=================

* POST Message
        
        :Slack "Message"
        
         
* POST Snippet
   
  Range selection change to the visual mode  
  
        :SlackSnippet {FileType} {Title}
  * Default FileType is "Python"
  * Default Title is "None"

* Show Channel History

        :SlackHistory {Limit}
 

* Show SlackChannels

        :SlackChannels

        
* Show Current channel

        :SlackChannel


* Set Channel

        :SlackChannels
   * Enter button to select the channel list that is displayed


License
=================
This software is released under the MIT License, see LICENSE.txt.