# new tunnel caps circa october 2021
Will the old caps work? 
Legacy caps: `tunnelIdentifier` and `parentTunnel`

Will the new caps work? 
new and latest caps: `tunnelName` and `tunnelOwner`

Will the results be the same across all platforms?
Answer: no

What happens when you mix the new caps w/ the old?
Answer: job errors out in most cases.

~~NOTE: May have found a problem where sub-accounts can use non-shared tunnels. I.e. tunnels missing the `--shared-tunnel` flag.~~ all is well nvm

### Tunnels Used
`./sc -u $SUPPORT_SUB_ACCOUNT -k $SUPPORT_SUB_ACCOUNT_KEY -i my-tunnel` tunnel owned by sub-account

`./sc -u $SUPPORT_TEAM_ADMIN -k $SUPPORT_TEAM_ADMIN_KEY --shared-tunnel` org wide tunnel shared by org admin



### Results
These results only show if a tunnel was used, not the test status.

##### Using A  Shared Tunnel
- Tunnel owned by org admin
- Tunnel has `--shared-tunnel`
- legacy == `tunnelIdentifier` + `parentTunnel` caps
- new == `tunnelName` + `tunnelOwner` caps

Shared
|cap type | VDC | RDC | VMD |
| --- | --- | --- | --- |
| legacy | :x: | :white_check_mark: | :white_check_mark: |
| new | :white_check_mark: | :white_check_mark: | :x: |


##### Using An Owned Tunnel
- Tunnel owned by sub-account or individual user
- Tunnel is not shared (no --shared-tunnel)
- no need for `parentTunnel` or `tunnelOwner` caps, ignoring these

Owned
|cap | VDC | RDC | VMD |
| --- | --- | --- | --- |
| tunnelIdentifier | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| tunnelName | :x: | :white_check_mark: | :x: |