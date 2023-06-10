# Street Fighter 6 Move Data

## Data Format

The data is saved as TOML in character-specific files.

### Move Type

The `moveType` property is a string representing the type of move.
The following table lists the possible values:

| Value           | Meaning                  |
|-----------------|--------------------------|
| `normal`        | Normal move              |
| `commandNormal` | Command normal move      |
| `action`        | Non-damaging actions     |
| `actionMove`    | Move requiring an action |
| `targetCombo`   | Target combo             |
| `special`       | Special move             |
| `super1`        | Level 1 super move       |
| `super2`        | Level 2 super move       |
| `super3`        | Level 3 super move       |
| `unique`        | Unique move              |
| `throw`         | Throw                    |

### Frame Count

The `frameCount` property is a list of values marking the various phase transitions. 
Each phase is represented by a letter followed by a dash and a number representing the last frame of that phase.
Here are all the possible values:

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

Note that invincibility frames are not included in the frame count, since they have they own property (see next section).

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

| Notation | Meaning       |
|----------|---------------|
| `1`      | Down-Back     |
| `2`      | Down          |
| `3`      | Down-Forward  |
| `4`      | Back          |
| `5`      | Neutral       |
| `6`      | Forward       |
| `7`      | Up-Back       |
| `8`      | Up            |
| `9`      | Up-Forward    |
| `d`      | Any direction |
| `[]`     | Simultaneous  |
| `()`     | Hold          |
| `>`      | Follow-up     |
| `|`      | Or            |
| `*p`     | Any punch     |
| `lp`     | Light Punch   |
| `mp`     | Medium Punch  |
| `hp`     | Heavy Punch   |
| `*k`     | Any kick      |
| `lk`     | Light Kick    |
| `mk`     | Medium Kick   |
| `hk`     | Heavy Kick    |
| `l*`     | Any light     |
| `m*`     | Any medium    |
| `h*`     | Any heavy     |
| `j*`     | Any jump      |
| `c*`     | Any crouch    |
| `pp`     | Any two *p    |
| `kk`     | Any two *k    |

### Cancels Into

This property lists the possible move types that a move can cancel into.
The following table lists the possible values:

| Value         | Meaning                     |
|---------------|-----------------------------|
| `chain`       | Chains into other normals   |
| `special`     | Cancels into special moves  |
| `super`       | Cancels into super moves    |
| `targetCombo` | Cancels into target combos  |
| `jump`        | Cancels into jump           |
| `super1`      | Cancels into level 1 supers |
| `super2`      | Cancels into level 2 supers |
| `super3`      | Cancels into level 3 supers |

### Block Type

The `blockType` property refers to the attack type with regards to blocking.

| Value      | Meaning  |
|------------|----------|
| `high`     | High     |
| `low`      | Low      |
| `overhead` | Overhead |
| `jumpIn`   | Jump-in  |

### Move Properties

The `properties` property is an object with the following properties:

| Property         | Description                                             |
|------------------|---------------------------------------------------------|
| `canCrossUp`     | Whether the move can cross up.                          |
| `armorBreak`     | Whether the move breaks armor.                          |
| `tumble`         | Whether the move causes a tumble state.                 |
| `juggle`         | Whether the move causes a juggle state.                 |
| `knockdown`      | Whether the move causes a knockdown state.              |
| `forcesStanding` | Whether the move forces the opponent to stand.          |
| `stockIncrement` | The amount of stock gained after performing the move.   |
| `stockDecrement` | The amount of stock consumed after performing the move. |
| `chargeable`     | Whether the move can be charged.                        |

## License

- The data and code are MIT-licensed.
- Game, character, and move names are copyright of their respective owners.
