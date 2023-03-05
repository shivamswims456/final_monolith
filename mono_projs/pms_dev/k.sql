--
-- Add field jelo to good
--
ALTER TABLE `good_good` ADD COLUMN `jelo` bigint UNSIGNED DEFAULT 1 NOT NULL CHECK (`jelo` >= 0);
ALTER TABLE `good_good` ALTER COLUMN `jelo` DROP DEFAULT;