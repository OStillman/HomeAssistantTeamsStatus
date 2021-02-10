# Home Assistant + Teams Status = Automation Glory

## What does it do?

- Tails the Teams Log for Status changes I.e. Away, Busy, Available etc.
- Updates a Home Assitant Sensor with these status changes
- Home Assistant then updates a Template Sensor to group these statuses better i.e. Busy, Inacall etc. all equal Busy
- Update a PiZero with Blinkt! running to change to Red, Green or Amber (Busy, Available, Away)
- Update on Workstation Lock/Unlock
  - Lock = Turn off Lights
  - Unlock = Lights on, assume Available
  - Also Switch the Room Lights on/off as desired

This also controls music!

- Home Assitant Toggle for Concentration required (for me this will play BBC Radio 1 if concentration **is not** needed, or BBC Radio 2 if concentration **is** required
- On Away, Busy, Locked or Laptop Off (described below) stop the music
- When back to availiable use the status of the Concentration toggle to play the correct Radio station

## How do I set this up?
I'll try and explain this in the coming days, for now, I'm populating this Repo with the required files
