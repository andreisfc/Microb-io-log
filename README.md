# Microb[io]log[y]

Fabio Carrer Andreis [andreisfc@protonmail.com]
2020

A prototype blog-type website for microorganism-related information. 

## Known issues:
 - New post always has 'admin' as author, regardless of which user is logged in. This is likely due to using the admin interface for additions;
 - Timezone is not localized, currently using Django default (UTC);
 - When adding repeated posts, raises an `IntegrityError` (due to the UNIQUE constraint in Post.slug), rather than catching and dealing with the exception;
 - Any user can edit, add or remove Posts, regardless of which user is the author. Ideally, these actions should be restricted to their respective authors;
 - Posts are currently limited to a single organism;

## Observations
The Post database was artificially populated and updated using the scrips in `mainpage/fcautils.py`. The Organism database was manually populated.
