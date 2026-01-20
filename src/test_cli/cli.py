from datetime import datetime
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.timer import Timer
from textual.reactive import reactive


class Clock(Static):
    """A widget to display the current time."""
    
    time = reactive("")
    
    def on_mount(self) -> None:
        """Set up the timer when the widget is mounted."""
        self.update_time()
        self.set_interval(1, self.update_time)
    
    def update_time(self) -> None:
        """Update the current time."""
        now = datetime.now()
        self.time = now.strftime("%H:%M:%S")
    
    def render(self) -> str:
        """Render the clock."""
        return self.time


class ClockApp(App[Timer]):
    """A simple full-screen clock TUI application."""
    
    CSS = """
    Screen {
        align: center middle;
    }
    
    Clock {
        width: 100%;
        height: 100%;
        content-align: center middle;
        text-style: bold;
        color: #00ff00;
        text-align: center;
    }
    """
    
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]
    
    def compose(self) -> ComposeResult:
        """Create the clock widget."""
        yield Clock()


def main():
    """Run the clock application."""
    app = ClockApp()
    app.run()


if __name__ == "__main__":
    main()
