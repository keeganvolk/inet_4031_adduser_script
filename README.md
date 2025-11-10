# INET4031 Add Users Script and User List

## Program Description

This python script automatically adds all users from an input file (see create-users.input) when ran. Normally, for each user that is to be added, one must run useradd to do so while either following the prompts or adding flags to input the information for that account. And in some cases, passwd must also be ran. This script automates all of that by using the useradd and passwd commands.

## Program User Operation

This script must be ran with sudo and python3 must be installed on the system. The lines within this script that contain `os.system()` are commented out to allow for testing before the commands are actually ran on the system.

### Command Execution
`sudo python3 create-users.py < create-users.input` can be used to run this script, or you can use `chmod +x create-users.py` to add the execute permission, then run `sudo ./create-users.py < create-users.input`.

### Input File Format
The create-users.input file can be replaced with another properly formatted input file.
The file format is as follows:

`[Username]:[Password]:[Last name]:[First name]:[Group1],[Group2],[etc...]`

For example:

`keeganv:securePassw0rd:Volk:Keegan:sysadmins,remoteusers`

Multiple groups are separated with commas. To not add a user to any groups, use `-` in place of the groups:

`[Username]:[Password]:[Last name]:[First name]:-`

To skip over a user in a file and NOT add them to your system, add `#` to the beginning of the line:

`#[Username]:[Password]:[Last name]:[First name]:[Group1]`

### "Dry Run"
To do a "dry run" of this script, you can leave the `os.system()` lines commented out. When you run the script like this, you will be able to view the printed output messages to see what is being done in order to debug the script BEFORE you let it make changes to your system.
