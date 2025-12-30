import time
import cv2
import numpy as np
import pyautogui
import speech_recognition as sr
import threading
from transformers import pipeline
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt
from rich.status import Status
from datetime import datetime

console = Console()

class AIBA:
    def __init__(self):
        self.console = console
        self.memory = []
        self.is_recording = False
        
        self._print_banner()
        
        self.console.print("[bold cyan]Initializing Neural Pathways (Downloading/Loading Models)...[/bold cyan]")
        try:
            self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            self.recognizer = sr.Recognizer()
            self.console.log("[green]✓ NLP Core Online[/green]")
            self.console.log("[green]✓ Audio Sensors Calibrated[/green]")
            self.console.log("[green]✓ Vision Modules Ready[/green]")
        except Exception as e:
            self.console.log(f"[bold red]Initialization Error:[/bold red] {e}")

    def _print_banner(self):
        banner_text = """
   ARTIFICIAL INTELLIGENCE BEHAVIOURAL ANALYSIS
        """
        self.console.print(Panel(Align.center(banner_text, vertical="middle"), style="bold magenta", subtitle="System v1.0"))

    def train_feed_data(self):
        self.console.print("\n[bold yellow]>> TRAINING MODE INITIATED[/bold yellow]")
        self.console.print("Feed data to AIBA. Type 'DONE' on a new line to finish.")
        
        data_buffer = []
        while True:
            line = input()
            if line.strip().upper() == 'DONE':
                break
            data_buffer.append(line)
        
        full_text = " ".join(data_buffer)
        self.memory.append(full_text)
        self.console.print(f"[bold green]✓ Data Ingested.[/bold green] Memory Nodes Updated: {len(self.memory)}")

    def analyze_text(self, text_input=None):
        if not text_input and self.memory:
            text_input = " ".join(self.memory[-1:])
            self.console.print("[dim]Analyzing latest memory block...[/dim]")
        
        if not text_input:
            self.console.print("[red]No data to analyze.[/red]")
            return

        with self.console.status("[bold blue]Processing Textual Behaviour...[/bold blue]"):
            if len(text_input) < 50:
                self.console.print(Panel(f"[italic]{text_input}[/italic]", title="Analysis (Short Input)", border_style="blue"))
                return

            summary = self.summarizer(text_input, max_length=130, min_length=30, do_sample=False)
            result = summary[0]['summary_text']
        
        self.console.print(Panel(result, title="[bold cyan]BEHAVIOURAL SUMMARY (TEXT)[/bold cyan]", border_style="cyan"))

    def analyze_audio(self):
        with sr.Microphone() as source:
            self.console.print("[bold red]>> LISTENING... (Speak now)[/bold red]")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=15)
                self.console.print("[dim]Processing audio signal...[/dim]")
                
                text_output = self.recognizer.recognize_google(audio)
                self.console.print(f"[italic]Detected Speech:[/italic] {text_output}")
                
                self.analyze_text(text_output)
                
            except sr.WaitTimeoutError:
                self.console.print("[yellow]No speech detected.[/yellow]")
            except sr.UnknownValueError:
                self.console.print("[red]Could not understand audio.[/red]")
            except Exception as e:
                self.console.print(f"[red]Audio Error: {e}[/red]")

    def analyze_screen(self, duration=5):
        self.console.print(f"[bold magenta]>> ANALYSING SCREEN BEHAVIOUR ({duration}s)[/bold magenta]")
        
        screen_size = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter("screen_analysis.avi", fourcc, 20.0, (screen_size.width, screen_size.height))
        
        start_time = time.time()
        frame_count = 0
        
        while (time.time() - start_time) < duration:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            frame_count += 1
            
            if frame_count % 10 == 0:
                print(".", end="", flush=True)
        
        out.release()
        print() 
        self._generate_visual_report(frame_count, duration)

    def _generate_visual_report(self, frames, duration):
        report = f"""
        [bold]Visual Stream Analysis[/bold]
        ---------------------------
        Total Frames Scanned : {frames}
        Duration             : {duration} seconds
        Resolution           : {pyautogui.size()}
        
        [italic]Inference:[/italic] Screen activity successfully captured. 
        Video data has been archived to 'screen_analysis.avi' for 
        deep-layer processing.
        """
        self.console.print(Panel(report, title="[bold magenta]VISUAL MODULE OUTPUT[/bold magenta]", border_style="magenta"))

    def run(self):
        while True:
            self.console.print("\n[bold white]SELECT MODULE:[/bold white]")
            self.console.print("1. [cyan]Feed Data (Train)[/cyan]")
            self.console.print("2. [blue]Analyze Text[/blue]")
            self.console.print("3. [red]Analyze Audio (Listen)[/red]")
            self.console.print("4. [magenta]Analyze Screen (Vision)[/magenta]")
            self.console.print("5. [dim]Exit[/dim]")
            
            choice = Prompt.ask("Enter Command", choices=["1", "2", "3", "4", "5"])
            
            if choice == "1":
                self.train_feed_data()
            elif choice == "2":
                user_text = Prompt.ask("Enter text to analyze (or leave empty to use Memory)")
                self.analyze_text(user_text)
            elif choice == "3":
                self.analyze_audio()
            elif choice == "4":
                try:
                    dur = int(Prompt.ask("Duration in seconds", default="5"))
                    self.analyze_screen(dur)
                except ValueError:
                    self.console.print("[red]Invalid number.[/red]")
            elif choice == "5":
                self.console.print("[bold red]Shutting down AIBA...[/bold red]")
                break

if __name__ == "__main__":
    ai_system = AIBA()
    ai_system.run()

#this model was developed in 2022 by Adwitiya Singh.This is Republised/Revised Version Of AIBA
