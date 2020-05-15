class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'copy'
        self.TarMirrorCommand = 'zip'
        self.CancelMirror = 'stop'
        self.CancelAllCommand = 'fall'
        self.ListCommand = 'list'
        self.StatusCommand = 'status'
        self.AuthorizeCommand = 'auth'
        self.UnAuthorizeCommand = 'unauth'
        self.PingCommand = 'ping'
        self.RestartCommand = 'restart'
        self.StatsCommand = 'stats'
        self.HelpCommand = 'help'
        self.LogCommand = 'log'
        self.CloneCommand = "clone"
        self.WatchCommand = 'watch'
        self.TarWatchCommand = 'tarwatch'

BotCommands = _BotCommands()
