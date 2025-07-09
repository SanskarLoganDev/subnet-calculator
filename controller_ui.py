from textual import on
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Footer, Header, Static, Input, Label, Button
from textual.binding import Binding

from subnet import Calculator

class CalculatorInputs(Static):
    
    def compose(self):
        yield Label("Enter IP Address")
        yield Input(placeholder="0.0.0.0", id="ip")
        yield Label("Enter Subnet Mask")
        yield Input(placeholder="Enter Subnet Mask: 32", id="mask")
        # Here you can add input fields for IP and mask, e.g., TextInput widgets
        
    @on(Input.Submitted)
    def handle_input(self):
        
        # Since there are two inputs, we need to handle them separately by using ids
        
        ip_input = self.query_one("#ip",Input)
        ip_address = ip_input.value.strip()

        mask_input = self.query_one("#mask",Input)
        subnet_mask = mask_input.value.strip()
        
        if not ip_address or not subnet_mask:
            self.query_one(Static).update("Please enter both IP address and subnet mask.")
            return
        result = Calculator()
        try:
            total_addresses, usable_addresses, network_address, broadcast_address = result.max_subnets(ip_address, int(subnet_mask))
            output = (
                f"Total Addresses: {total_addresses}\n"
                f"Usable Addresses: {usable_addresses}\n"
                f"Network Address: {network_address}\n"
                f"Broadcast Address: {broadcast_address}"
            )
        except Exception as e:
            output = f"Error: {e}"
        
        self.mount(Label(output))

class SubnetCalculator(App):
    # Bindings = ("key", action name, "description")
    # In bindings mention the action name without "action_" prefix
    BINDINGS = [
        Binding("d", "toggle_dark_mode", "Toggle Dark Mode", priority=True),
    ]
    
    CSS_PATH = "calculator.css"
    
    def compose(self):
        # widgets that will be used in the UI
        yield Header(show_clock=True, name="Subnet Calculator")
        with ScrollableContainer(): 
            yield CalculatorInputs()
            yield Button("Exit")
        yield Footer()
        
        
    # action name must start with "action_"
    def action_toggle_dark_mode(self):
        self.theme = "textual-light" if self.theme == "textual-dark" else "textual-dark"
    
    @on(Button.Pressed)
    def action_exit(self):
        self.exit()

if __name__ == "__main__":
    SubnetCalculator().run()
    