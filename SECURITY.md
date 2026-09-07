# Security and Sanitization

Before publishing your own fork, scan for:

- API keys and tokens;
- OAuth values;
- passwords/passcodes;
- chat/user IDs;
- email addresses not intended for publication;
- home-directory usernames;
- internal IPs/hosts;
- private repository URLs;
- client/project names;
- task IDs and cron IDs that reveal internal operations;
- protected identity/canon content.

Recommended checks:

```bash
grep -RniE 'sk-|token|password|secret|oauth|api[_-]?key' .
grep -RniE '/Users/|/home/|chat_id|user_id' .
```

Use a secret scanner before public release when possible.
