import random 

def execute():
  auditd_types = ["SYSCALL", "USER_AUTH", "USER_CMD", "LOGIN", "CWD", "PATH", "FILE"]
  selected_audit_type = auditd_types[random.randint(0, len(auditd_types)) - 1]
  pid_number = random.randint(1000, 9999)
  print(f"type={selected_audit_type} msg=audit(XXXXXXXXXXXXXXX): pid={pid_number} uid=")

if __name__ == "__main__":
  execute()
