# personal configuration could/should be added in a separate file
if [ -f ~/.bash_config ]; then
. ~/.bash_config
fi

# >> .bash_config
# Add time stamp to history
# see strftime documentation for other formatting options
# the last space allows to add a space with the content - this is not a typo :)
HISTTIMEFORMAT="%F %T %z $ "