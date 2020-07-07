## Automated ELK Stack Deployment

The files in this repository were used to configure the network depicted below.

![TODO: Update the path with the name of your diagram](Pictures/'Saved Pictures'/Diagram1.png)

These files have been tested and used to generate a live ELK deployment on Azure. They can be used to either recreate the entire deployment pictured above. Alternatively, select portions of the _____ file may be used to install only certain pieces of it, such as Filebeat.

  - _TODO: filebeat-playbook.yml

This document contains the following details:
- Description of the Topologu
- Access Policies
- ELK Configuration
  - Beats in Use
  - Machines Being Monitored
- How to Use the Ansible Build


### Description of the Topology

The main purpose of this network is to expose a load-balanced and monitored instance of DVWA, the D*mn Vulnerable Web Application.

Load balancing ensures that the application will be highly Available, in addition to restricting Access to the network.
- _TODO: What aspect of security do load balancers protect? What is the advantage of a jump box? It gives you a direct IP to SSH from that is already protected with an SSH key. It just makes it extra secure.

Integrating an ELK server allows users to easily monitor the vulnerable VMs for changes to the Logs and system Logs.
- _TODO: What does Filebeat watch for? Filebeat allows me to monitor the logs remotely. It collects the logs and forwards them to Elasticsearch or Logstash.
- _TODO: What does Metricbeat record? Metric beat lets you record metrics from the system such as Apache and HAProxy.

The configuration details of each machine may be found below.
_Note: Use the [Markdown Table Generator](http://www.tablesgenerator.com/markdown_tables) to add/remove values from the table_.

| Name             | Function | IP Address | Operating System |
|------------------|----------|------------|------------------|
| Jump Box         | Gateway  | 10.0.0.1   | Linux            |
| Web-1            | Monitor  | 10.0.0.5   | Linux            |
| Web-2            | Monitor  | 10.0.0.6   | Linux            |
| Central-Park Elk | ElkServer| 10.1.0.4   | Linux            |

### Access Policies

The machines on the internal network are not exposed to the public Internet. 

Only the Jump-Box machine can accept connections from the Internet. Access to this machine is only allowed from the following IP addresses:
- _TODO: Add whitelisted IP addresses 184.96.92.185

Machines within the network can only be accessed by Jump-Box.
- _TODO: Which machine did you allow to access your ELK VM? What was its IP address? Jump-Box 52.229.29.229

A summary of the access policies in place can be found in the table below.

| Name     | Publicly Accessible | Allowed IP Addresses |
|----------|---------------------|----------------------|
| Jump Box | Yes                 | 184.96.92.185        |
| Web-1    | No                  | 10.0.0.4             |
| Web-2    | No                  | 10.0.0.4             |

### Elk Configuration

Ansible was used to automate configuration of the ELK machine. No configuration was performed manually, which is advantageous because...
- _TODO: What is the main advantage of automating configuration with Ansible? It can be saved and run on any new machine. This is something that can be added to your bag of goodies to know how to run something on start.

The playbook implements the following tasks:
- _TODO: In 3-5 bullets, explain the steps of the ELK installation play. E.g., install Docker; download image; etc._
- Install docker
- download image
- run asible playbook

The following screenshot displays the result of running `docker ps` after successfully configuring the ELK instance.

![TODO: Update the path with the name of your screenshot of docker ps output](Pictures/'Saved Pictures'/elasticday1.png)

### Target Machines & Beats
This ELK server is configured to monitor the following machines:
- _TODO: List the IP addresses of the machines you are monitoring 
- 10.0.0.5
- 10.0.0.6

We have installed the following Beats on these machines:
- _TODO: Specify which Beats you successfully installed Filebeat

These Beats allow us to collect the following information from each machine:
- _TODO: In 1-2 sentences, explain what kind of data each beat collects, and provide 1 example of what you expect to see. E.g., `Winlogbeat` collects Windows logs, which we use to track user logon events, etc._
- Filebeat collects log data and sends it back to elasticsearch
### Using the Playbook
In order to use the playbook, you will need to have an Ansible control node already configured. Assuming you have such a control node provisioned: 

SSH into the control node and follow the steps below:
- Copy the Ansible-config file to the ansible container.
- Update the host file to include... the right IP addresses and uncomment the default username
- Run the playbook, and navigate to Web-1 to check that the installation worked as expected.

_TODO: Answer the following questions to fill in the blanks:_
- _Which file is the playbook? Where do you copy it?_
- ansible-playbook.yml you copy it to the ansible container
- _Which file do you update to make Ansible run the playbook on a specific machine? How do I specify which machine to install the ELK server on versus which to install Filebeat on?_
- ansible.cfg the host file and what you edit is how to specify which machine to install the elk servers on
- _Which URL do you navigate to in order to check that the ELK server is running?
- the IPAdress of your ELK server/TCP

_As a **Bonus**, provide the specific commands the user will need to run to download the playbook, update the files, etc._