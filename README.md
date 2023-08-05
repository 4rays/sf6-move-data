# Street Fighter 6 Move Data

## Data Format

The data is saved as TOML in character-specific files.

### Move Type

The `moveType` property is a string representing the type of the move.
The following table lists the possible values:

| Value           | Meaning                  |
|-----------------|--------------------------|
| `normal`        | Normal move              |
| `commandNormal` | Command normal move      |
| `action`        | Non-damaging actions     |
| `followUp`      | Move requiring an action |
| `targetCombo`   | Target combo             |
| `special`       | Special move             |
| `super1`        | Level 1 super move       |
| `super2`        | Level 2 super move       |
| `super3`        | Level 3 super move       |
| `unique`        | Unique move              |
| `throw`         | Throw                    |
| `commandThrow`  | Command throw            |

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
| `{360}`  | 360 motion    |
| `()`     | Simultaneous  |
| `[]`     | Hold          |
| `>`      | Follow-up     |
| `{|}`    | Or            |
| `*p`     | Any punch     |
| `lp`     | Light Punch   |
| `mp`     | Medium Punch  |
| `hp`     | Heavy Punch   |
| `*k`     | Any kick      |
| `lk`     | Light Kick    |
| `mk`     | Medium Kick   |
| `hk`     | Heavy Kick    |
| `d`      | Any direction |
| `j`      | Any jump      |
| `c`      | Any crouch    |
| `pp`     | Any two *p    |
| `kk`     | Any two *k    |

### Cancel

This property lists the possible move types that a move can cancel into.
The following table lists the possible values:

| Value | Meaning                                                |
|-------|--------------------------------------------------------|
| `C`   | Can be canceled by a special move, DI, DR, or SA       |
| `SA`  | Can only be canceled by a Super Art                    |
| `SA2` | Can only be canceled by a level 2 or level 3 Super Art |
| `SA3` | Can only be canceled by a level 3 Super Art            |
| `J`   | Can be canceled by a jump                              |
| `*`   | Can be canceled by other moves. See `cancelsInto`.     |

### Block Type

The `blockType` property refers to the attack type with regards to blocking.

| Value  | Meaning  |
|--------|----------|
| `high` | High     |
| `low`  | Low      |
| `mid`  | Overhead |
| `midHigh` | High or overhead |

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

- The code is MIT-licensed.
- Game, character, and move names and data are copyright of their respective owners.
