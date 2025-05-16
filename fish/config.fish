if status is-interactive
    	# Commands to run in interactive sessions can go here
	set brewcmd (path filter /opt/homebrew/bin/brew /usr/local/bin/brew)[1] and $brewcmd shellenv | source
end
