---
date: 2026-09-15
course: 普通物理
chapter: "Ch01 Measurement"
tags:
  - 普通物理
  - Physics
  - Measurement
status: learning
---

# General Physics — Ch01 Measurement

> [!summary] 本章重點
> - 物理實驗的核心是以可比較、可重現的方式測量 physical quantities。
> - measurement 是把物理量和標準（standard）比較，並用適當的 unit 表示結果。
> - SI 使用七個 base quantities；其他 physical quantities 可由它們組合成 derived quantities。
> - SI-derived units 可寫回 SI base units，例如 joule 與 watt。
> - scientific notation 與 SI prefixes 用來簡潔表示很大或很小的量。
> - chain-link conversion 讓數值與單位一起運算，conversion factor 的值等於 1。
> - meter、second、kilogram 的標準需要穩定、可取得，並且盡量不隨時間改變。
> - significant figures 反映測量結果中真正有意義的位數；density 則把 mass 與 volume 聯繫起來。

---

## 1. Measurement

### 1.1 Measuring Things

Science and engineering 建立在對 **physical quantities** 的精確測量與比較上。為了讓不同測量可以互相比較，需要：

- **Rules**：說明如何測量、如何比較。
- **Units**：表示測量量值的方式。
- 物理學的一個目的，就是設計並進行實驗，以建立可使用的 rules 與 units。

### Physical Quantities

第一次出現的定義：**物理量（physical quantity）** 是實驗中需要測量的物理性質或量。

PDF 列出的例子包括：

- length
- mass
- pressure
- time
- temperature
- electric current

測量每一個 physical quantity 時，都要把它和一個 **standard** 比較；因此，測量本質上不是只讀取一個數字，而是用標準來表達「這個量相當於多少個 unit」。

### Units and Standards

| 概念 | 意義 | 例子 |
| --- | --- | --- |
| quantity | 被測量的物理量 | length |
| unit | 給某一物理量的測量所使用的專門名稱 | meter（m） |
| standard | 與被測量量比較、且恰好對應該 quantity 的 `1.0` unit 的參考標準 | length 的 meter standard |

以 `Length — Meter (m)` 為例：

- `Length` 是 quantity。
- `meter` 是 unit，`m` 是 unit symbol。
- meter 的 standard 定義了什麼叫作 `1.0 m`。

一個適合作為 base standard 的標準，應該具備：

- **Accessible**：可以取得、使用。
- **Invariable**：隨時間不改變，測量不會因時間而改變。

## SI Base Quantities

physical quantities 很多，而且不一定彼此獨立，例如 length 與 speed 有關。PDF 選出七個 **base quantities**，它們各自被指定 standard，並用來定義其他 physical quantities。

| Physical quantity | 中文 | SI unit | Symbol |
| --- | --- | --- | --- |
| Time | 時間 | second | `s` |
| Length | 長度 | meter | `m` |
| Mass | 質量 | kilogram | `kg` |
| Electric current | 電流 | ampere | `A` |
| Thermodynamic temperature | 熱力學溫度 | kelvin | `K` |
| Amount of substance | 物質的量 | mole | `mol` |
| Luminous intensity | 發光強度 | candela | `cd` |

**base quantity** 的角色：

- 是一組選定的、彼此作為基礎的 physical quantities。
- 每個 base quantity 都有相對應的 standard。
- 其他 physical quantities 可由 base quantities 定義，這些就是 **derived quantities**。

例如 speed 由 length 與 time 組成：

$$
\text{speed}=\frac{\text{length}}{\text{time}}
$$

在 SI 中，若 length 用 `m`、time 用 `s`，speed 的單位就是 `m/s`。

## SI-Derived Units

**SI-derived unit** 是用 SI base units 定義出的單位。PDF 中的例子如下。

### Energy：joule

$$
1\,\mathrm{J}=1\,\mathrm{kg}\cdot\mathrm{m}^{2}/\mathrm{s}^{2}
$$

Joule（`J`）是 energy 的 SI unit；寫成 base units 時，可看出它由 kilogram、meter 與 second 組成。

### Power：watt

$$
1\,\mathrm{W}=1\,\mathrm{J}/\mathrm{s}
$$

$$
1\,\mathrm{W}=1\,\mathrm{kg}\cdot\mathrm{m}^{2}/\mathrm{s}^{3}
$$

Watt（`W`）是 power 的 SI unit，表示每單位時間所對應的 energy transfer；因此它等於 joule per second。

## Scientific Notation

**Scientific notation** 用來表示非常大或非常小的 quantities，核心是用 power of 10 改寫數字。

PDF 中的例子：

$$
3\,560\,000\,000\,\mathrm{m}=3.56\times10^{9}\,\mathrm{m}
$$

$$
0.000\,000\,492\,\mathrm{s}=4.92\times10^{-7}\,\mathrm{s}
$$

在電腦表示法中，`E` 代表「乘上 10 的某次方」：

- `3.56E9 m` = `3.56 × 10^9 m`
- `4.92E-7 s` = `4.92 × 10^-7 s`

因此，`E9` 表示乘以 `10^9`，`E-7` 表示乘以 `10^{-7}`。

## SI Prefixes

**Prefix** 放在 unit 前面，用來表示某個 power of 10。PDF 的 SI prefixes 如下：

| Factor | Prefix | Symbol |
| ---: | --- | --- |
| `10^24` | yotta- | `Y` |
| `10^21` | zetta- | `Z` |
| `10^18` | exa- | `E` |
| `10^15` | peta- | `P` |
| `10^12` | tera- | `T` |
| `10^9` | giga- | `G` |
| `10^6` | mega- | `M` |
| `10^3` | kilo- | `k` |
| `10^2` | hecto- | `h` |
| `10^1` | deka- | `da` |
| `10^{-1}` | deci- | `d` |
| `10^{-2}` | centi- | `c` |
| `10^{-3}` | milli- | `m` |
| `10^{-6}` | micro- | `μ` |
| `10^{-9}` | nano- | `n` |
| `10^{-12}` | pico- | `p` |
| `10^{-15}` | femto- | `f` |
| `10^{-18}` | atto- | `a` |
| `10^{-21}` | zepto- | `z` |
| `10^{-24}` | yocto- | `y` |

課堂特別標示、較常使用的 prefixes：

- giga-：`G`，`10^9`
- mega-：`M`，`10^6`
- kilo-：`k`，`10^3`
- centi-：`c`，`10^{-2}`
- milli-：`m`，`10^{-3}`
- micro-：`μ`，`10^{-6}`
- nano-：`n`，`10^{-9}`
- pico-：`p`，`10^{-12}`

PDF 中的例子：

$$
1.27\times10^{9}\,\mathrm{W}=1.27\,\mathrm{gigawatts}=1.27\,\mathrm{GW}
$$

$$
2.35\times10^{-9}\,\mathrm{s}=2.35\,\mathrm{nanoseconds}=2.35\,\mathrm{ns}
$$

## Unit Conversion

### Chain-link conversion

改變 unit 時，使用 **chain-link conversion**：把原本的 quantity 乘上一個 **conversion factor**。

Conversion factor 是「數值與單位一起構成、且整體等於 1 的比值」。例如：

$$
\frac{60\,\mathrm{s}}{1\,\mathrm{min}}=1
$$

因為 `1 min` 與 `60 s` 代表同一段時間，所以這個比值等於 1。乘上它時，數值與 unit 會重新表示，但實際的物理量不會改變。

> [!important]
> 單位本身也要像代數量一樣一起運算。若把 `min` 放在分母，就可以和原本量中的 `min` 約掉。

### Example：2 min → seconds

$$
2\,\mathrm{min}
\times
\frac{60\,\mathrm{s}}{1\,\mathrm{min}}
=120\,\mathrm{s}
$$

運算時，原本的 `min` 與 conversion factor 分母的 `min` 消掉，最後留下 `s`。

## Length

meter 的 standard 曾經歷多次改變。PDF 的歷史整理如下：

1. **地球尺度**：定義為從 North Pole 到 equator 距離的千萬分之一。
2. **實物標準**：使用存放在 France 的 platinum-iridium standard meter bar。
3. **光譜標準**：使用 krypton-86 原子發出的 orange-red light，以 `1,650,763.73` 個波長定義長度。

> [!info] 補充
> 從地理、實物標準逐步改成以自然現象為基礎，是為了讓 standard 更容易重現，也不必依賴單一物件的保存狀態。

> [!important] Definition
> The meter is the length of the path traveled by light in a vacuum during a time interval of `1/299 792 458` of a second.

換句話說，現代 meter definition 把光在真空中的路徑長度，和精確的 time interval 綁在一起。

## Significant Figures

**有效位數（significant figures）** 是測量數值中有意義、且對 measurement resolution 有貢獻的 digits。計算結果通常要配合輸入量中最少的 significant figures 做 rounding。

### 判斷規則

1. **所有非零數字都是有效位數。**

   - `91` 有 2 個 significant figures：`9`、`1`。
   - `123.45` 有 5 個 significant figures：`1`、`2`、`3`、`4`、`5`。

2. **兩個非零數字中間的 0 是有效位數。**

   - `101.1203` 有 7 個 significant figures：`1`、`0`、`1`、`1`、`2`、`0`、`3`。

3. **Leading zeros 不是有效位數。**

   - `0.00052` 只有 2 個 significant figures：`5`、`2`。
   - 前面的 0 只是在定位小數點，不表示測量精度。

4. **含有 decimal point 的數字，其 trailing zeros 是有效位數。**

   - `12.2300` 有 6 個 significant figures：`1`、`2`、`2`、`3`、`0`、`0`。
   - 小數點後的尾端 0 表示測量保留到那一位，因此不能任意刪掉。

### Rounding examples

#### `11.3516` → 3 significant figures

保留前三個 significant figures：`1`、`1`、`3`。下一位是 `5`，所以第三位 `3` 往上進位：

$$
11.3516\longrightarrow11.4
$$

#### `11.3279` → 3 significant figures

同樣保留前三個 significant figures：`1`、`1`、`3`。下一位是 `2`，小於 `5`，所以不進位：

$$
11.3279\longrightarrow11.3
$$

> [!warning] 常見錯誤
>
> - 不要看到 `0` 就直接判定它不是有效位數。
> - 要分清楚 leading zero 與 trailing zero。
> - `101.1203` 中間的 0 要計入；`0.00052` 前面的 0 不計入；`12.2300` 小數點後的尾端 0 要計入。

## 1.2 Time

在 scientific work 中，我們常需要知道一個 event 持續多久。因此，任何 time standard 都必須回答兩件事：

- **When did it happen?**：它在什麼時候發生？
- **What is its duration?**：它持續了多久？

### Standard of time

- **Rotation of Earth**：用來決定 length of a day，但地球自轉並非足夠穩定。
- **Quartz clocks**：利用 quartz 持續振動作為週期性的參考。
- **Atomic clocks**：利用 atom 的穩定特性作為更一致的時間標準。

> [!important] Definition — Second
> One second is the time taken by `9 192 631 770` oscillations of the light (of a specified wavelength) emitted by a cesium-133 atom.

Atomic clock 比 Earth rotation 更適合作為 standard，因為它的讀值更一致。PDF 給的比較是：兩個 cesium clocks 必須運轉 `6000 years`，讀值才會相差超過 `1 s`。這也顯示了 atomic clocks 的 precision，以及 Earth rotation 的相對不精確。

### Some approximate time intervals

| Measurement | Time interval in seconds |
| --- | ---: |
| Lifetime of the proton（predicted） | `3 × 10^40` |
| Age of the universe | `5 × 10^17` |
| Age of the pyramid of Cheops | `1 × 10^11` |
| Human life expectancy | `2 × 10^9` |
| Length of a day | `9 × 10^4` |
| Time between human heartbeats | `8 × 10^{-1}` |
| Lifetime of the muon | `2 × 10^{-6}` |
| Shortest lab light pulse | `1 × 10^{-16}` |
| Lifetime of the most unstable particle | `1 × 10^{-23}` |
| The Planck time | `1 × 10^{-43}` |

## 1.3 Mass

### Kilogram standard

PDF 介紹的 SI mass standard 是一個存放在 France 的 platinum（鉑）與 iridium（銥）合金圓柱：

- 它代表一個 mass of one kilogram。
- 精確 copies 被送到世界各地。
- 其他 masses 可以和這些 copies 比較來測量。

### Atomic mass unit

**Atomic mass unit（u）** 是另一個 mass standard，適合描述 atom 與 molecule 的質量。

- 一個 Carbon-12 atom 被指定為 `12 u`。
- PDF 給出的換算值為：

$$
1\,\mathrm{u}=1.66053886\times10^{-27}\,\mathrm{kg}
\quad(\pm10\times10^{-35}\,\mathrm{kg})
$$

- `u` 主要用於測量 atoms 與 molecules 的 masses。

## Density

Density（密度，$\rho$，發音為 *rho*）定義為單位體積所含的 mass：

$$
\rho=\frac{m}{V}
$$

其中：

- $\rho$：density
- `m`：mass
- `V`：volume

SI unit 為：

$$
\mathrm{kg/m^3}
$$

### Density equation 的三種基本變形

由

$$
\rho=\frac{m}{V}
$$

可整理出：

$$
m=\rho V
$$

$$
V=\frac{m}{\rho}
$$

使用時先確認題目要求的是 density、mass 還是 volume，再選擇對應的形式。

### PDF examples

$$
\text{Density of material}
=\frac{18\,\mathrm{kg}}{0.032\,\mathrm{m^3}}
=560\,\mathrm{kg/m^3}
$$

$$
\text{Mass of object}
=(380\,\mathrm{kg/m^3})(0.0040\,\mathrm{m^3})
=1.5\,\mathrm{kg}
$$

$$
\text{Volume of object}
=\frac{250\,\mathrm{kg}}{1280\,\mathrm{kg/m^3}}
=0.20\,\mathrm{m^3}
$$

## Problems

以下集中整理 PDF 中的 Sample Problem 與 Practice。PDF 沒有提供完整解答的題目，下面補上推導；使用 PDF 沒列出的常數或幾何關係時，會明確標示。

### Sample Problem 1.1.1

**題目**

The largest ball of string in the world is about `2 m` in radius. To the nearest order of magnitude, find the total length `L` of string in the ball. Assume the string has a square cross-section with edge length `d = 4 mm`.

**已知**

- Ball radius：`r = 2 m`
- String cross-section edge：`d = 4 mm = 4 × 10^{-3} m`

**要求**

- String total length `L`
- To the nearest order of magnitude

**核心觀念**

把線球視為球體，球的 volume 等於線的 volume；線的 volume 等於 cross-sectional area 乘上 length。

> [!info] 補充
> PDF 題目沒有列出球體體積公式與「線的 volume = cross-sectional area × length」的幾何關係。以下只補上解這一題所需的最少內容。

> [!example] 解題
> **Given**
>
> `r = 2 m`，`d = 4 × 10^{-3} m`
>
> **Conversion factor**
>
> `1 mm = 10^{-3} m`
>
> **Calculation**
>
> 球體 volume：
>
> $$
> V_{\mathrm{ball}}=\frac{4}{3}\pi r^3
> =\frac{4}{3}\pi(2\,\mathrm{m})^3
> \approx33.5\,\mathrm{m^3}
> $$
>
> 線的 cross-sectional area：
>
> $$
> A=d^2=(4\times10^{-3}\,\mathrm{m})^2
> =1.6\times10^{-5}\,\mathrm{m^2}
> $$
>
> 因為 `V_ball = A L`，所以：
>
> $$
> L=\frac{V_{\mathrm{ball}}}{A}
> =\frac{33.5\,\mathrm{m^3}}{1.6\times10^{-5}\,\mathrm{m^2}}
> \approx2.1\times10^6\,\mathrm{m}
> $$
>
> **Answer**
>
> `L ≈ 2.1 × 10^6 m`，所以取最近的 order of magnitude 為：
>
> $$
> \boxed{L\sim10^6\,\mathrm{m}}
> $$

### Practice 01

**題目**

1. `1.3 km → ? m`
2. `0.8 km → ? cm`
3. `2845 mm → ? ft`

> [!example] 解題
> **Given**
>
> `1.3 km`、`0.8 km`、`2845 mm`
>
> **Conversion factor**
>
> `1 km = 10^3 m`，`1 m = 10^2 cm`
>
> **Calculation**
>
> 1. $$
> 1.3\,\mathrm{km}
> \times\frac{10^3\,\mathrm{m}}{1\,\mathrm{km}}
> =1.3\times10^3\,\mathrm{m}
> $$
>
> 2. $$
> 0.8\,\mathrm{km}
> \times\frac{10^3\,\mathrm{m}}{1\,\mathrm{km}}
> \times\frac{10^2\,\mathrm{cm}}{1\,\mathrm{m}}
> =8\times10^4\,\mathrm{cm}
> $$
>
> 3. 這一小題需要 PDF 沒有列出的 inch、foot 轉換：
>
> $$
> 2845\,\mathrm{mm}
> \times\frac{1\,\mathrm{in}}{25.4\,\mathrm{mm}}
> \times\frac{1\,\mathrm{ft}}{12\,\mathrm{in}}
> \approx9.334\,\mathrm{ft}
> $$
>
> **Answer**
>
> 1. `1.3 × 10^3 m`
> 2. `8 × 10^4 cm`
> 3. `9.334 ft`（依 `2845 mm` 的 4 位有效位數保留）

> [!info] 補充
> Practice 01 第 3 題的 `ft` conversion factor 沒有出現在 PDF；解題使用 `1 ft = 12 in` 與 `1 in = 25.4 mm`。

### Sample Problem 1.2.1

**題目**

Light-fermi 是光走過 `1 fermi` 的時間，其中 `1 fermi = 1 femtometer = 1 fm`。問一個 light-fermi 有多少秒？

**已知**

- `1 fm = 10^{-15} m`（由 PDF 的 femto- prefix）
- 光速 `c = 3.00 × 10^8 m/s`

**要求**

- Light-fermi 對應的 time

> [!info] 補充
> PDF 沒有列出 light speed 的數值；以下使用標準近似 `c = 3.00 × 10^8 m/s`，只補上本題所需的常數。

> [!example] 解題
> **Given**
>
> `d = 1 fm = 10^{-15} m`，`c = 3.00 × 10^8 m/s`
>
> **Conversion factor**
>
> `femto- = 10^{-15}`
>
> **Calculation**
>
> 由 `c = d/t`，解出 `t = d/c`：
>
> $$
> t=\frac{d}{c}
> =\frac{1\times10^{-15}\,\mathrm{m}}
> {3.00\times10^8\,\mathrm{m/s}}
> =3.33\times10^{-24}\,\mathrm{s}
> $$
>
> **Answer**
>
> $$
> \boxed{1\ \text{light-fermi}\approx3.3\times10^{-24}\,\mathrm{s}}
> $$

### Practice 02

**題目**

The height of a motion picture film is `35.0 cm`. If `24 frames` go by in `1.0 s`, calculate the total number of frames required to show a `2.0 h` long motion picture.

**已知**

- Film height：`35.0 cm`
- Frame rate：`24 frames/s`
- Movie duration：`2.0 h`

**要求**

- Total number of frames

> [!example] 解題
> **Given**
>
> `24 frames/s`，`2.0 h`
>
> **Conversion factor**
>
> `1 h = 60 min`，`1 min = 60 s`
>
> **Calculation**
>
> 先將電影長度換成 seconds，再乘上每秒的 frames：
>
> $$
> N
> =2.0\,\mathrm{h}
> \times\frac{60\,\mathrm{min}}{1\,\mathrm{h}}
> \times\frac{60\,\mathrm{s}}{1\,\mathrm{min}}
> \times\frac{24\,\mathrm{frames}}{1\,\mathrm{s}}
> $$
>
> $$
> N=172\,800\,\mathrm{frames}
> \approx1.7\times10^5\,\mathrm{frames}
> $$
>
> **Answer**
>
> $$
> \boxed{N\approx1.7\times10^5\ \text{frames}}
> $$
>
> `35.0 cm` 是題目提供但這個計算不需要的資料；本題只需要 frame rate 與 movie duration。

### Practice 03

**題目**

The age of the universe is approximately `10^10 years`, and mankind has existed for about `10^6 years`. If the age of the universe were `1.0 day`, how many seconds would mankind have existed？

**已知**

- Age of the universe：`10^10 years`
- Mankind：`10^6 years`
- PDF table 的 length of a day：`9 × 10^4 s`

**要求**

- Scaled duration of mankind in seconds

> [!example] 解題
> **Given**
>
> Universe age `10^10 years`，mankind age `10^6 years`，scaled universe age `1 day`
>
> **Conversion factor**
>
> `1 day ≈ 9 × 10^4 s`（使用 PDF 的 approximate time interval）
>
> **Calculation**
>
> 人類存在時間占宇宙年齡的比例：
>
> $$
> \frac{10^6\,\mathrm{years}}{10^{10}\,\mathrm{years}}
> =10^{-4}
> $$
>
> 因此，在把宇宙年齡縮成一天後：
>
> $$
> t
> =10^{-4}\times9\times10^4\,\mathrm{s}
> =9\,\mathrm{s}
> $$
>
> **Answer**
>
> $$
> \boxed{t\approx9\,\mathrm{s}}
> $$

### Sample Problem 1.3.1

**題目**

A heavy object may sink into ground during an earthquake if shaking causes liquefaction. For a ground sample, the void ratio is

$$
e=\frac{V_{\mathrm{voids}}}{V_{\mathrm{grains}}}
$$

where $V_{\mathrm{grains}}$ is the total volume of sand grains and $V_{\mathrm{voids}}$ is the total volume between grains. If $e$ exceeds the critical value `0.8`, liquefaction can occur. Find the corresponding sand density $\rho_{\mathrm{sand}}$. Solid silicon dioxide, the primary component of sand, has density `2.6 × 10^3 kg/m^3`.

**已知**

- Critical void ratio：`e_c = 0.8`
- Grain material density：$\rho_{\mathrm{grains}}=2.6\times10^3\,\mathrm{kg/m^3}$
- `e = V_voids / V_grains`

**要求**

- Critical corresponding bulk sand density $\rho_{\mathrm{sand}}$

**核心觀念**

Sand sample 的 total volume 不只有 grains，還包括 grains 之間的 voids：

$$
V_{\mathrm{total}}=V_{\mathrm{grains}}+V_{\mathrm{voids}}
$$

> [!info] 補充
> PDF 題目給了 void ratio，但沒有把 sand 的 bulk density 推導完整寫出。以下只補上由 mass 與 total volume 定義 density 所需的代數推導。

> [!example] 解題
> **Given**
>
> $e_c=0.8$，$\rho_{\mathrm{grains}}=2.6\times10^3\,\mathrm{kg/m^3}$
>
> **Conversion factor**
>
> 由 `e = V_voids / V_grains` 得：
>
> $$
> V_{\mathrm{voids}}=eV_{\mathrm{grains}}
> $$
>
> **Calculation**
>
> Total volume：
>
> $$
> V_{\mathrm{total}}
> =V_{\mathrm{grains}}+V_{\mathrm{voids}}
> =V_{\mathrm{grains}}(1+e)
> $$
>
> Sand 中的 mass 來自 solid grains，因此：
>
> $$
> m=\rho_{\mathrm{grains}}V_{\mathrm{grains}}
> $$
>
> 代入 sand 的 density 定義：
>
> $$
> \rho_{\mathrm{sand}}
> =\frac{m}{V_{\mathrm{total}}}
> =\frac{\rho_{\mathrm{grains}}V_{\mathrm{grains}}}
> {V_{\mathrm{grains}}(1+e)}
> =\frac{\rho_{\mathrm{grains}}}{1+e}
> $$
>
> 在 critical value `e_c = 0.8` 時：
>
> $$
> \rho_{\mathrm{sand,critical}}
> =\frac{2.6\times10^3\,\mathrm{kg/m^3}}{1+0.8}
> =1.44\times10^3\,\mathrm{kg/m^3}
> \approx1.4\times10^3\,\mathrm{kg/m^3}
> $$
>
> **Answer**
>
> 臨界對應的 sand density 約為：
>
> $$
> \boxed{\rho_{\mathrm{sand,critical}}\approx1.4\times10^3\,\mathrm{kg/m^3}}
> $$
>
> 因為 liquefaction 的條件是 `e > 0.8`，所以實際上 `e` 超過臨界值時，bulk sand density 會低於這個臨界值。

### Practice 04

**題目**

Gold has a density of `19.32 g/cm^3`.

1. If a sample of gold with a mass of `29.34 g` is pressed into a leaf of `1.000 μm` thickness, what is the area of the leaf？
2. If the gold is drawn out into a cylindrical fiber of radius `2.5 μm`, what is the length of the fiber？

**已知**

- Gold density：$\rho=19.32\,\mathrm{g/cm^3}$
- Gold mass：`m = 29.34 g`
- Leaf thickness：`t = 1.000 μm`
- Fiber radius：`r = 2.5 μm`

> [!info] 補充
> PDF 沒有在 prefix 表之外列出 `μm` 與 `cm` 的換算步驟；以下使用 `1 μm = 10^{-4} cm`。圓柱體積關係 `V = A L` 也是本題必要的幾何補充。

#### (a) Area of the gold leaf

> [!example] 解題
> **Given**
>
> $m=29.34\,\mathrm{g}$，$\rho=19.32\,\mathrm{g/cm^3}$，$t=1.000\,\mu\mathrm{m}$
>
> **Conversion factor**
>
> $$
> 1\,\mu\mathrm{m}=10^{-4}\,\mathrm{cm}
> $$
>
> **Calculation**
>
> 先由 density 求 gold 的 volume：
>
> $$
> V=\frac{m}{\rho}
> =\frac{29.34\,\mathrm{g}}{19.32\,\mathrm{g/cm^3}
> }\approx1.5186\,\mathrm{cm^3}
> $$
>
> Leaf volume `V = A t`，所以：
>
> $$
> A=\frac{V}{t}
> =\frac{1.5186\,\mathrm{cm^3}}
> {1.000\times10^{-4}\,\mathrm{cm}}
> =1.5186\times10^4\,\mathrm{cm^2}
> $$
>
> **Answer**
>
> $$
> \boxed{A\approx1.519\times10^4\,\mathrm{cm^2}=1.519\,\mathrm{m^2}}
> $$

#### (b) Length of the cylindrical fiber

> [!example] 解題
> **Given**
>
> `V = 1.5186 cm^3`，`r = 2.5 μm`
>
> **Conversion factor**
>
> $$
> r=2.5\,\mu\mathrm{m}=2.5\times10^{-4}\,\mathrm{cm}
> $$
>
> **Calculation**
>
> 圓柱的 cross-sectional area：
>
> $$
> A_{\mathrm{cross}}
> =\pi r^2
> =\pi(2.5\times10^{-4}\,\mathrm{cm})^2
> \approx1.9635\times10^{-7}\,\mathrm{cm^2}
> $$
>
> 由 `V = A_cross L`：
>
> $$
> L=\frac{V}{A_{\mathrm{cross}}}
> =\frac{1.5186\,\mathrm{cm^3}}
> {1.9635\times10^{-7}\,\mathrm{cm^2}}
> \approx7.734\times10^6\,\mathrm{cm}
> $$
>
> $$
> 7.734\times10^6\,\mathrm{cm}
> \times\frac{1\,\mathrm{m}}{100\,\mathrm{cm}}
> =7.734\times10^4\,\mathrm{m}
> $$
>
> **Answer**
>
> 受半徑 `2.5 μm` 的 2 位有效位數限制：
>
> $$
> \boxed{L\approx7.7\times10^4\,\mathrm{m}\approx77\,\mathrm{km}}
> $$

## 📌 Exam Review

### Definitions

- **Physical quantity**：需要測量並以標準比較的物理量。
- **Unit**：給某一 physical quantity 的測量所使用的專門名稱。
- **Standard**：對應 quantity 的 `1.0` unit、用來比較測量的參考。
- **Base quantity**：被選作基礎、並用來定義其他 physical quantities 的 quantity。
- **SI-derived unit**：用 SI base units 組合定義出的 unit。
- **Significant figures**：測量值中有意義、反映 measurement resolution 的 digits。
- **Density**：mass per unit volume，$\rho=m/V$。

### Equations

$$
\text{speed}=\frac{\text{length}}{\text{time}}
$$

$$
1\,\mathrm{J}=1\,\mathrm{kg}\cdot\mathrm{m^2/s^2}
$$

$$
1\,\mathrm{W}=1\,\mathrm{J/s}=1\,\mathrm{kg}\cdot\mathrm{m^2/s^3}
$$

$$
\rho=\frac{m}{V},\qquad m=\rho V,\qquad V=\frac{m}{\rho}
$$

### Units

- SI base units：`s`、`m`、`kg`、`A`、`K`、`mol`、`cd`
- Derived units：`J`（joule）、`W`（watt）
- 常用 prefixes：`G = 10^9`、`M = 10^6`、`k = 10^3`、`c = 10^{-2}`、`m = 10^{-3}`、`μ = 10^{-6}`、`n = 10^{-9}`、`p = 10^{-12}`
- Prefix symbols 要注意大小寫，例如 `M` 是 mega，而 `m` 是 milli。

### Common Mistakes

1. 把 quantity、unit、standard 混為一談。
2. 做 unit conversion 時只換數字，忘記一起處理 units。
3. 沒有讓 conversion factor 中的原單位消掉。
4. 混淆 prefix symbol 的大小寫，例如 `M`、`m`、`k`。
5. 把 leading zeros 當成 significant figures。
6. 忘記兩個非零數字中間的 0 是 significant figure。
7. 忘記 decimal number 的 trailing zeros 可能是 significant figures。
8. rounding 時沒有看保留位數後的下一個 digit。
9. density 題目中把 $m/V$、$\rho V$、$m/\rho$ 三種形式用錯。
10. 題目提供的資料不一定全部都會用到，例如 Practice 02 的 `35.0 cm`。

### Questions I Should Be Able to Answer

- [ ] 什麼是 physical quantity？
- [ ] quantity、unit、standard 差在哪？
- [ ] 七個 SI base quantities 是什麼？
- [ ] 如何用 conversion factor 做單位轉換？
- [ ] 如何判斷 significant figures？
- [ ] meter、second、kilogram 的標準概念是什麼？
- [ ] density 公式如何變形？
