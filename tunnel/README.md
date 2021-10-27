# new tunnel caps circa october 2021
Will the old caps work? 
Legacy caps: `tunnelIdentifier` and `parentTunnel`

Will the new caps work? 
new and latest caps: `tunnelName` and `tunnelOwner`

Will the results be the same across all platforms?

What happens when you mix the new caps w/ the old?


~~NOTE: May have found a problem where sub-accounts can use non-shared tunnels. I.e. tunnels missing the `--shared-tunnel` flag.~~ all is well nvm

### Results

Using A  Shared Tunnel
|cap type | VDC | RDC | VMD |
| --- | --- | --- | --- |
| legacy | :x: | :white_check_mark: | ? |
| new | :white_check_mark: | :white_check_mark: | ? |


Using An Owned Tunnel
|cap | VDC | RDC | VMD |
| --- | --- | --- | --- |
| tunnelIdentifier | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| tunnelName | :x: | :white_check_mark: | :x: |