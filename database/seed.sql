#roles

INSERT INTO roles (role_id, name, description)
VALUES
(gen_random_uuid(), 'Administrator', 'Full access'),
(gen_random_uuid(), 'Laboratory Staff', 'Laboratory management'),
(gen_random_uuid(), 'Coordinator', 'Academic coordinator'),
(gen_random_uuid(), 'Student', 'Read only access');

#categories

INSERT INTO categories (category_id, name, description)
VALUES
(gen_random_uuid(), 'Measurement Equipment', 'Measurement instruments'),
(gen_random_uuid(), 'Development Boards', 'Embedded systems'),
(gen_random_uuid(), 'Computers', 'Desktop and laptops'),
(gen_random_uuid(), 'Specialized Machinery', 'Industrial equipment'),
(gen_random_uuid(), 'Tools', 'Manual tools'),
(gen_random_uuid(), 'Cables', 'Communication and power cables'),
(gen_random_uuid(), 'Soldering Equipment', 'Soldering and repair equipment');