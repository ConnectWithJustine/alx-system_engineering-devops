## Task 0

**Postmortem Report: Service Outage on 24th January 2024**

**Issue Summary:**

*Duration:* The outage occurred on 1/24/2024 from 3:00 pm to 9:00 pm, GMT+1.

*Impact:* The service affected was the File Share Service. Users experienced slow response times. Approximately 20% of users were affected.

*Root Cause:* The root cause of the outage was identified as Server Overload.

---

**Timeline:**

- *Detection Time:* The issue was detected on 1/24/2024 at 6:00 pm.

- *Detection Method:* A monitoring alert was triggered.

- *Actions Taken:*
  - Investigated Loadbalancer server.
  - Assumed root cause to be a DDoS attack.
  - Explored Web Server 1.
  - Escalated incident to system admin.
  
- *Resolution Time:* The incident was resolved on 24/1/2024 at 8:45 pm.

---

**Root Cause and Resolution:**

*Root Cause:* The issue stemmed from an overwhelming number of requests leading to server overload. High traffic resulted in slow response times.

*Resolution:* The problem was addressed by optimizing server resources, distributing load more efficiently, and implementing performance improvements.

---

**Corrective and Preventative Measures:**

*Improvements/Fixes:*
1. Enhance monitoring on critical components to promptly identify and respond to potential overloads.
2. Update system dependencies to ensure compatibility and optimal performance.

*Tasks:*
1. Patch Nginx server to address potential vulnerabilities and enhance performance.
2. Implement additional monitoring for server memory to proactively manage resource usage.
3. Conduct a comprehensive review of the entire File Share System/Process to identify and address any other potential bottlenecks.
4. Collaborate with the DevOps Engineer to enhance the incident escalation process, ensuring a more efficient and timely response to future incidents.

---
