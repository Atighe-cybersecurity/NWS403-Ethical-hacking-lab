# NWS403 – Ethical Hacking Practical Lab 1

## Project Overview

This project is a beginner-level ethical hacking practical developed as part of my NWS403 Ethical Hacking and Penetration Testing studies.

The practical involved creating a local Python-based web server and performing controlled security tests using Kali Linux tools.

The purpose was to understand how web services operate, how open ports can be identified, and how basic security mechanisms such as rate limiting behave.

## Objectives

- Create and run a simple Python web server.
- Identify an open port using Nmap.
- Perform HTTP requests using cURL.
- Understand HTTP response codes.
- Test basic rate-limiting behaviour.
- Examine the purpose and limitations of robots.txt.
- Collect and verify practical evidence.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Kali Linux | Testing environment |
| Python 3 | Running the web server |
| Nmap | Port and service discovery |
| cURL | Sending HTTP requests |
| Git | Version control |
| GitHub | Project hosting |

## Lab Environment

- Operating System: Kali Linux
- Target IP: 127.0.0.1 (localhost)
- Target Port: 8080
- Web Server: Python HTTP server
- Testing Environment: Local virtual machine

## Practical Activities

### 1. Starting the Web Server

The Python script `hims_lab_target.py` was executed to start the local web server.

```bash
python3 hims_lab_target.py
```

The server listened on:

```text
http://127.0.0.1:8080
```

### 2. Port Scanning with Nmap

The following command was used:

```bash
nmap -sV -p 8080 -T2 127.0.0.1
```

**Result:** Port 8080 was identified as open, and the service was identified as an HTTP service running on Python.

### 3. HTTP Testing with cURL

cURL was used to send HTTP requests to the local server.

Example:

```bash
curl -I http://127.0.0.1:8080/internal/payroll_demo.txt
```

**Result:** The server returned HTTP 200 OK and response headers to the HEAD request.

### 4. Rate-Limiting Test

A series of HTTP requests was sent to examine how the server handled repeated requests.

**Observed results:**
- Requests 1–8 returned HTTP 200.
- Requests 9–12 returned HTTP 429 (Too Many Requests).

This demonstrated the rate-limiting mechanism implemented in the lab server.

### 5. Examining robots.txt

The following command was used:

```bash
curl -s http://127.0.0.1:8080/robots.txt
```

The server returned instructions disallowing crawlers from accessing `/internal/`.

This exercise demonstrated that robots.txt provides crawler instructions but does not enforce access control or protect sensitive resources.

### 6. Evidence Collection and Integrity

The response headers were saved in an evidence file:

```bash
curl -I http://127.0.0.1:8080/internal/payroll_demo.txt > evidence_log.txt
```

A SHA-256 hash was generated:

```bash
sha256sum evidence_log.txt
```

This hash can be used to check whether the evidence file has changed.

### 7. Cleaning Up

After testing, the Python server was stopped and Nmap was used again to check port 8080.

The port was identified as closed because no service was listening on it.

## Key Findings

- Nmap can identify open ports and running services.
- cURL can be used to interact with HTTP services.
- HTTP status codes provide information about server responses.
- Rate limiting can help control excessive requests.
- robots.txt is not a security mechanism.
- SHA-256 can help verify evidence integrity.

## Limitations

- Testing was performed on localhost only.
- The practical used a simulated environment, not a real company's network.
- The HEAD request demonstrated a successful response but did not demonstrate an authentication bypass.
- The rate-limiting test applied to the GET request handler implemented in this lab.

## Learning Outcomes

Through this practical, I gained hands-on experience with:

- Basic Linux terminal operations.
- Python web server execution.
- Network and service discovery.
- HTTP request testing.
- Basic web security concepts.
- Evidence collection and documentation.
- Git and GitHub version control.

## Ethical Considerations

All tests were conducted in a controlled local environment for educational purposes.

No external systems were targeted. The practical followed the principles of authorized security testing and responsible evidence collection.

## Author

**Atighe Peace Bongabi**

BTech Cybersecurity Student

GitHub: [@Atighe-cybersecurity](https://github.com/Atighe-cybersecurity)
