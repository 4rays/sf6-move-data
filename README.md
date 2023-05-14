# Street Fighter 6 Move Data

## Data Format

The data is saved as JSON in character-specific separate files.

### Frame Count

The `frameCount` property is a list of values representing the _last frame index_ for each phase.
Here is a description of all the possible values:

| Value | Meaning           |
|-------|-------------------|
| S     | Pre-startup       |
| A     | Active            |
| R     | Recovery          |
| PA    | Projectile-active |

So for Ryu's standing light punch, the `frameCount` property value is formatted as follows:

```json
"frameCount": ["S-3", "A-6", "R-13"]
```

This reads as follows:

- The pre-startup phase ends on frame 3, which means frame 4 and onward are active.
- The active phase ends on frame 6, which means frame 7 and onward are recovery.
- The recovery phase ends on frame 13, the last frame of the move.

In the game frame meter UI, the move looks like the following:

<img src="https://github.com/4rays/sf6-move-data/blob/5a367d1a20cbff5246c9a7b025ce42650aab16a3/example.png" width="300" />

### Invincibility Frames

Invincibility frames are represented as an object with the following properties:

| Property          | Type   | Description                                  |
|-------------------|--------|----------------------------------------------|
| `start`           | Number | The first frame of invincibility.            |
| `end`             | Number | The last frame of invincibility.             |
| `projectileStart` | Number | The first frame of projectile invincibility. |
| `projectileEnd`   | Number | The last frame of projectile invincibility.  |
| `strikeStart`     | Number | The first frame of strike invincibility.     |
| `strikeEnd`       | Number | The last frame of strike invincibility.      |
| `airStart`        | Number | The first frame of air move invincibility.   |
| `airEnd`          | Number | The last frame of air move invincibility.    |

Each pair of `*start` and `*end` values represents a range of frames where the character is invincible.
Both values need to be present, even if the range is only one frame long.

### Input

The `input` property is a string representing the input required to perform the move.
The following table lists the special notation used in the string:

| Notation | Meaning      |
|----------|--------------|
| `1`      | Down-Back    |
| `2`      | Down         |
| `3`      | Down-Forward |
| `4`      | Back         |
| `5`      | Neutral      |
| `6`      | Forward      |
| `7`      | Up-Back      |
| `8`      | Up           |
| `9`      | Up-Forward   |
| `[]`     | Simultaneous |
| `()`     | Hold         |
| `>`      | Follow-up    |
| `lp`     | Light Punch  |
| `mp`     | Medium Punch |
| `hp`     | Heavy Punch  |
| `lk`     | Light Kick   |
| `mk`     | Medium Kick  |
| `hk`     | Heavy Kick   |
| `j`      | Jump         |
| `pp`     | Any two p*   |
| `kk`     | Any two k*   |

### Cancels Into

This property lists the possible move types that a move can cancel into.
The following table lists the possible values:

| Value         | Meaning                     |
|---------------|-----------------------------|
| `chain`       | Chains into other normals   |
| `special`     | Cancels into special moves  |
| `super`       | Cancels into super moves    |
| `targetCombo` | Cancels into target combos  |
| `superLevel1` | Cancels into level 1 supers |
| `superLevel2` | Cancels into level 2 supers |
| `superLevel3` | Cancels into level 3 supers |


### Move Properties

The `properties` property is an object with the following properties:

| Property         | Description                                             |
|------------------|---------------------------------------------------------|
| `canCrossUp`     | Whether the move can cross up.                          |
| `armorBreak`     | Whether the move breaks armor.                          |
| `tumble`         | Whether the move causes a tumble state.                 |
| `knockdown`      | Whether the move causes a knockdown state.              |
| `forcesStanding` | Whether the move forces the opponent to stand.          |
| `stockIncrement` | The amount of stock gained after performing the move.   |
| `stockDecrement` | The amount of stock consumed after performing the move. |
