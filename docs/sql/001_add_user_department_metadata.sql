ALTER TABLE public.audit_logs
ADD COLUMN user_id VARCHAR(50) NOT NULL DEFAULT 'unknown_user';

ALTER TABLE public.audit_logs
ADD COLUMN department VARCHAR(100) NOT NULL DEFAULT 'Unknown';