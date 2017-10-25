## 2. Csvstack ##

/home/dq$ head -5 Combined_hud.csv

## 3. Csvlook ##

/home/dq$ head -10 Combined_hud.csv | csvlook

## 4. Csvcut ##

/home/dq$ csvcut -c 2 Combined_hud.csv | head -10

## 5. Csvstat ##

/home/dq$ csvstat Combined_hud.csv --mean

## 6. Csvcut | csvstat ##

/home/dq$ csvstat -c 2 Combined_hud.csv

## 7. Csvgrep ##

/home/dq$ csvgrep -c 2 -m -9 Combined_hud.csv | head -10 | csvlook

## 8. Filtering out problematic rows ##

/home/dq$ csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only.csv