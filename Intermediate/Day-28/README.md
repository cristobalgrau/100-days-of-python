# Day 28 - Tkinter, Dynamic Typing and the Pomodoro GUI Application

## Project: Pomodoro App

The Pomodoro GUI Application is a productivity tool based on the Pomodoro Technique, a time management method developed 
by Francesco Cirillo in the late 1980s. This application helps users stay focused and productive by breaking work into 
intervals separated by short breaks. It allows users to customize work and break durations and provides visual and auditory 
cues to guide them through each interval.

### Key Features:

- **Customizable Timer:** Users can set the duration of work sessions (in minutes) using the WORK_MIN constant, as well as the durations of short breaks (SHORT_BREAK_MIN) and long breaks (LONG_BREAK_MIN). These durations can be adjusted according to individual preferences and productivity needs.
- **Countdown Mechanism:** The application includes a countdown timer that displays the remaining time for each work or break session. The timer updates dynamically, ticking down seconds until the session is complete.
- **Timer Mechanism:** The timer alternates between work sessions and breaks based on the Pomodoro Technique. After completing a set number of work sessions (determined by the reps variable), the application triggers a long break to provide users with an extended rest period.
- **User Interface (UI) Setup:** The graphical user interface (GUI) features a clean and intuitive design, with a tomato image representing the traditional Pomodoro timer. Buttons for starting and resetting the timer are provided, along with a label to display the current timer status (work or break) and a section for displaying checkmarks to track completed work sessions.
- **Timer Reset:** Users can reset the timer at any time using the "Reset" button. This functionality allows them to restart the Pomodoro cycle or make adjustments to the timer settings as needed.
- **Window Popup Notification:** When the work session timer reaches zero, a window pops up to notify the user that it's time for a break. This feature ensures that users are alerted when each work session ends, prompting them to take a rest and transition into the next phase of the Pomodoro cycle.

### Libraries, Classes, and Widgets:

- `tkinter`: Python's standard GUI (Graphical User Interface) toolkit used for creating graphical applications.
- `Tk()`: Represents the main window or root window of the application.
- `Canvas()`: Widget for drawing graphics, such as images and text, on the interface.
- `Label()`: Widget used to display static text on the interface.
- `Button()`: Widget that triggers an action or function when clicked by the user.

### Implementation:

The "Pomodoro GUI Application" is developed using the `Tkinter` library in Python. The application employs constants to set the durations of work sessions and breaks. 
These constants allow for easy customization of session lengths according to user preferences.

The core functionality of the timer is managed by the `start_timer()` function, which tracks the progress of each session. Using a global variable reps, the function keeps count of the number of sessions completed, determining whether to initiate a work session, short break, or long break based on the current count. This approach ensures adherence to the Pomodoro Technique's alternating work and break intervals.

To visualize the countdown, the application leverages the `Canvas` widget provided by Tkinter. The canvas displays a tomato image as a visual representation of the timer, with the timer_text item updating dynamically to reflect the remaining time in each session. This dynamic updating is achieved through the `count_down()` function, which recursively calls itself with a one-second delay until the countdown reaches zero.

One notable feature of the implementation is the use of `window.deiconify()` to bring the application window to the foreground when a work session ends. This action ensures that users are promptly notified of the transition to a break period, promoting adherence to the Pomodoro Technique's time management principles. Additionally, the interface includes buttons for starting and resetting the timer, providing users with convenient controls for managing their work sessions.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/18141046-7a59-4911-acd4-4250001840b8)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/84c0c73e-741e-460e-856e-f4b5c4cd21a0)


