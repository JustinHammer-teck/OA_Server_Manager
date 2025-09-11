========================
CODE SNIPPETS
========================
TITLE: OBS-WebSocket Hello Message Example (Authentication Not Required)
DESCRIPTION: Example of a 'Hello' message (OpCode 0) from the obs-websocket server when authentication is not required, showing only version information.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_7

LANGUAGE: json
CODE:
```
{
  "op": 0,
  "d": {
    "obsStudioVersion": "30.2.2",
    "obsWebSocketVersion": "5.5.2",
    "rpcVersion": 1
  }
}
```

----------------------------------------

TITLE: OBS-WebSocket Hello Message Example (Authentication Required)
DESCRIPTION: An example of the 'Hello' message (OpCode 0) sent by the obs-websocket server when client authentication is mandatory, including the 'challenge' and 'salt' fields.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_5

LANGUAGE: json
CODE:
```
{
  "op": 0,
  "d": {
    "obsStudioVersion": "30.2.2",
    "obsWebSocketVersion": "5.5.2",
    "rpcVersion": 1,
    "authentication": {
      "challenge": "+IxH4CnCiqpX1rM9scsNynZzbOe4KhDeYcTNS3PDaeY=",
      "salt": "lM1GncleQOaCu9lT1yeUZhFYnqhsLLP1G5lAGo3ixaI="
    }
  }
}
```

----------------------------------------

TITLE: OBS-WebSocket Hello Message Example (Authentication Required)
DESCRIPTION: Example of a 'Hello' message (OpCode 0) from the obs-websocket server when authentication is required, including 'challenge' and 'salt' for client processing.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_6

LANGUAGE: json
CODE:
```
{
  "op": 0,
  "d": {
    "obsStudioVersion": "30.2.2",
    "obsWebSocketVersion": "5.5.2",
    "rpcVersion": 1,
    "authentication": {
      "challenge": "+IxH4CnCiqpX1rM9scsNynZzbOe4KhDeY=",
      "salt": "lM1GncleQOaCu9lT1yeUZhFYnqhsLLP1G5lAGo3ixaI="
    }
  }
}
```

----------------------------------------

TITLE: OBS-WebSocket Authentication Challenge Object Example
DESCRIPTION: Example of the 'authentication' object sent by the server in the 'Hello' message, containing the 'challenge' and 'salt' for client authentication.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_2

LANGUAGE: json
CODE:
```
{
    "challenge": "+IxH4CnCiqpX1rM9scsNynZzbOe4KhDeY=",
    "salt": "lM1GncleQOaCu9lT1yeUZhFYnqhsLLP1G5lAGo3ixaI="
}
```

----------------------------------------

TITLE: OBS-WebSocket Hello Message Example (Authentication Not Required)
DESCRIPTION: An example of the 'Hello' message (OpCode 0) sent by the obs-websocket server when client authentication is not required, omitting the 'authentication' field.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_6

LANGUAGE: json
CODE:
```
{
  "op": 0,
  "d": {
    "obsStudioVersion": "30.2.2",
    "obsWebSocketVersion": "5.5.2",
    "rpcVersion": 1
  }
}
```

----------------------------------------

TITLE: Start Virtual Camera Output (OBS-Websocket API)
DESCRIPTION: Initiates the virtual camera output. This is a direct command to activate the virtual camera.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_250

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Start Replay Buffer Output (OBS-Websocket API)
DESCRIPTION: Initiates the replay buffer output. This is a direct command to activate the replay buffer.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_254

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Start Record Output API
DESCRIPTION: Initiates the recording process for the OBS record output.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_272

LANGUAGE: APIDOC
CODE:
```
Method: StartRecord
Description: Starts the record output.
Details:
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
```

----------------------------------------

TITLE: Start Stream API for OBS WebSocket
DESCRIPTION: Initiates the OBS stream output.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_267

LANGUAGE: APIDOC
CODE:
```
StartStream:
  Request: None
  Response: None
```

----------------------------------------

TITLE: GetVideoSettings
DESCRIPTION: Gets the current video settings. Note: To get the true FPS value, divide the FPS numerator by the FPS denominator. Example: 60000/1001

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_164

LANGUAGE: APIDOC
CODE:
```
Method: GetVideoSettings
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  fpsNumerator: Number - Numerator of the fractional FPS value
  fpsDenominator: Number - Denominator of the fractional FPS value
  baseWidth: Number - Width of the base (canvas) resolution in pixels
  baseHeight: Number - Height of the base (canvas) resolution in pixels
  outputWidth: Number - Width of the output resolution in pixels
  outputHeight: Number - Height of the output resolution in pixels
```

----------------------------------------

TITLE: Start Output API for OBS WebSocket
DESCRIPTION: Initiates a specified OBS output. Requires the output name as input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_261

LANGUAGE: APIDOC
CODE:
```
StartOutput:
  Request:
    outputName: String - Output name
  Response: None
```

----------------------------------------

TITLE: ObsOutputState Enumeration
DESCRIPTION: Defines the possible states of an OBS output, such as starting, started, stopping, or stopped.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_23

LANGUAGE: APIDOC
CODE:
```
ObsOutputState:
  OBS_WEBSOCKET_OUTPUT_UNKNOWN
  OBS_WEBSOCKET_OUTPUT_STARTING
  OBS_WEBSOCKET_OUTPUT_STARTED
  OBS_WEBSOCKET_OUTPUT_STOPPING
  OBS_WEBSOCKET_OUTPUT_STOPPED
  OBS_WEBSOCKET_OUTPUT_RECONNECTING
  OBS_WEBSOCKET_OUTPUT_RECONNECTED
  OBS_WEBSOCKET_OUTPUT_PAUSED
  OBS_WEBSOCKET_OUTPUT_RESUMED
```

----------------------------------------

TITLE: Example obs-websocket Event Documentation: StudioModeStateChanged
DESCRIPTION: Demonstrates the JSDoc-like comment for the `StudioModeStateChanged` event, showing how to document its data fields, type, subscription, complexity, RPC version, initial version, and category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/README.md#_snippet_3

LANGUAGE: JavaScript
CODE:
```
/**
 * Studio mode has been enabled or disabled.
 *
 * @dataField studioModeEnabled | Boolean | True == Enabled, False == Disabled
 *
 * @eventType StudioModeStateChanged
 * @eventSubscription General
 * @complexity 1
 * @rpcVersion -1
 * @initialVersion 5.0.0
 * @category general
 * @api events
 */
```

----------------------------------------

TITLE: Example obs-websocket Enum Documentation: WebSocketOpCode::Hello
DESCRIPTION: Illustrates the JSDoc-like comment for the `WebSocketOpCode::Hello` enum, showing how to document its identifier, value, type, RPC version, initial version, and API category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/README.md#_snippet_1

LANGUAGE: JavaScript
CODE:
```
/**
* The initial message sent by obs-websocket to newly connected clients.
*
* @enumIdentifier Hello
* @enumValue 0
* @enumType WebSocketOpCode
* @rpcVersion -1
* @initialVersion 5.0.0
* @api enums
*/
```

----------------------------------------

TITLE: Get Input Settings (OBS WebSocket API)
DESCRIPTION: Gets the settings of an input. Note: Does not include defaults. To create the entire settings object, overlay `inputSettings` over the `defaultInputSettings` provided by `GetInputDefaultSettings`. This API endpoint has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_191

LANGUAGE: APIDOC
CODE:
```
GetInputSettings:
  Description: Gets the settings of an input. Note: Does not include defaults. To create the entire settings object, overlay inputSettings over the defaultInputSettings provided by GetInputDefaultSettings.
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input to get the settings of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input to get the settings of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
  Response Fields:
    inputSettings:
      Type: Object
      Description: Object of settings for the input
    inputKind:
      Type: String
      Description: The kind of the input
```

----------------------------------------

TITLE: Get Current Preview Scene (OBS-WebSocket API)
DESCRIPTION: Gets the current preview scene. Only available when studio mode is enabled. This request is slated to have the `currentPreview`-prefixed fields removed from in an upcoming RPC version.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_177

LANGUAGE: APIDOC
CODE:
```
GetCurrentPreviewScene
  Description: Gets the current preview scene.
  Note: Only available when studio mode is enabled. This request is slated to have the `currentPreview`-prefixed fields removed from in an upcoming RPC version.
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Response Fields:
    sceneName: String - Current preview scene name
    sceneUuid: String - Current preview scene UUID
    currentPreviewSceneName: String - Current preview scene name
    currentPreviewSceneUuid: String - Current preview scene UUID
```

----------------------------------------

TITLE: OBS-WebSocket Authentication Challenge Object Example
DESCRIPTION: Illustrates the JSON structure of the authentication challenge and salt provided by the obs-websocket server within its 'Hello' message, used for client authentication.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_2

LANGUAGE: json
CODE:
```
{
    "challenge": "+IxH4CnCiqpX1rM9scsNynZzbOe4KhDeYcTNS3PDaeY=",
    "salt": "lM1GncleQOaCu9lT1yeUZhFYnqhsLLP1G5lAGo3ixaI="
}
```

----------------------------------------

TITLE: Get Current Program Scene (OBS-WebSocket API)
DESCRIPTION: Gets the current program scene. This request is slated to have the `currentProgram`-prefixed fields removed from in an upcoming RPC version.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_175

LANGUAGE: APIDOC
CODE:
```
GetCurrentProgramScene
  Description: Gets the current program scene.
  Note: This request is slated to have the `currentProgram`-prefixed fields removed from in an upcoming RPC version.
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Response Fields:
    sceneName: String - Current program scene name
    sceneUuid: String - Current program scene UUID
    currentProgramSceneName: String - Current program scene name (Deprecated)
    currentProgramSceneUuid: String - Current program scene UUID (Deprecated)
```

----------------------------------------

TITLE: Request (OpCode 6)
DESCRIPTION: Client is making a request to obs-websocket. Eg get current scene, create source.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_12

LANGUAGE: APIDOC
CODE:
```
Sent from: Identified client
Sent to: obs-websocket

Data Keys:
{
  "requestType": string,
  "requestId": string,
  "requestData": object(optional),

}

Example Message:
{
  "op": 6,
  "d": {
    "requestType": "SetCurrentProgramScene",
    "requestId": "f819dcf0-89cc-11eb-8f0e-382c4ac93b9c",
    "requestData": {
      "sceneName": "Scene 12"
    }
  }
}
```

----------------------------------------

TITLE: GetStudioModeEnabled
DESCRIPTION: Gets whether studio is enabled.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_283

LANGUAGE: APIDOC
CODE:
```
Response Fields:
  studioModeEnabled (Boolean): Whether studio mode is enabled.
```

----------------------------------------

TITLE: Get Source Filter Default Settings
DESCRIPTION: Gets the default settings for a specific filter kind.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_223

LANGUAGE: APIDOC
CODE:
```
GetSourceFilterDefaultSettings:
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    filterKind: String - Filter kind to get the default settings for.
  Response Fields:
    defaultFilterSettings: Object - Object of default settings for the filter kind.
```

----------------------------------------

TITLE: OBS-WebSocket Authentication String Generation Steps
DESCRIPTION: Step-by-step guide on how to generate the client authentication string using SHA256 hashing and Base64 encoding, based on the server-provided 'salt' and 'challenge'.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_3

LANGUAGE: APIDOC
CODE:
```
Authentication String Creation Steps:
- Concatenate the websocket password with the salt provided by the server (password + salt)
- Generate an SHA256 binary hash of the result and base64 encode it, known as a base64 secret.
- Concatenate the base64 secret with the challenge sent by the server (base64_secret + challenge)
- Generate a binary SHA256 hash of that result and base64 encode it. You now have your authentication string.
```

----------------------------------------

TITLE: Get Source Filter List
DESCRIPTION: Gets an array of all filters applied to a specified source.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_222

LANGUAGE: APIDOC
CODE:
```
GetSourceFilterList:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    sourceName: String - Name of the source (Optional).
    sourceUuid: String - UUID of the source (Optional).
  Response Fields:
    filters: Array<Object> - Array of filters.
```

----------------------------------------

TITLE: Get Source Filter Kind List
DESCRIPTION: Gets an array of all available source filter kinds. This is similar to 'GetInputKindList'.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_221

LANGUAGE: APIDOC
CODE:
```
GetSourceFilterKindList:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in v5.4.0
  Response Fields:
    sourceFilterKinds: Array<String> - Array of source filter kinds.
```

----------------------------------------

TITLE: Example obs-websocket Request Documentation: GetPersistentData
DESCRIPTION: Illustrates the JSDoc-like comment for the `GetPersistentData` request, showing how to document its request parameters (realm, slotName) and response fields (slotValue), along with its type, complexity, RPC version, initial version, and category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/README.md#_snippet_5

LANGUAGE: JavaScript
CODE:
```
/**
 * Gets the value of a "slot" from the selected persistent data realm.
 *
 * @requestField realm    | String | The data realm to select. `OBS_WEBSOCKET_DATA_REALM_GLOBAL` or `OBS_WEBSOCKET_DATA_REALM_PROFILE`
 * @requestField slotName | String | The name of the slot to retrieve data from
 *
 * @responseField slotValue | String | Value associated with the slot. `null` if not set
 *
 * @requestType GetPersistentData
 * @complexity 2
 * @rpcVersion -1
 * @initialVersion 5.0.0
 * @category config
 * @api requests
 */
```

----------------------------------------

TITLE: GetCurrentSceneTransition
DESCRIPTION: Gets information about the current scene transition.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_214

LANGUAGE: APIDOC
CODE:
```
GetCurrentSceneTransition:
  Description: Gets information about the current scene transition.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Response Fields:
    - transitionName (String): Name of the transition
    - transitionUuid (String): UUID of the transition
    - transitionKind (String): Kind of the transition
    - transitionFixed (Boolean): Whether the transition uses a fixed (unconfigurable) duration
    - transitionDuration (Number): Configured transition duration in milliseconds. `null` if transition is fixed
    - transitionConfigurable (Boolean): Whether the transition supports being configured
    - transitionSettings (Object): Object of settings for the transition. `null` if transition is not configurable
```

----------------------------------------

TITLE: Example Successful RequestResponse Message (OpCode 7) - obs-websocket
DESCRIPTION: This JSON snippet provides an example of a successful 'RequestResponse' message from obs-websocket. It shows the opcode '7', mirrors the client's request type and ID, and indicates success within the 'requestStatus' object.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_16

LANGUAGE: json
CODE:
```
{
  "op": 7,
  "d": {
    "requestType": "SetCurrentProgramScene",
    "requestId": "f819dcf0-89cc-11eb-8f0e-382c4ac93b9c",
    "requestStatus": {
      "result": true,
      "code": 100
    }
  }
}
```

----------------------------------------

TITLE: Get Input List API Documentation
DESCRIPTION: Retrieves an array of all inputs currently configured in OBS. The list can optionally be restricted to inputs of a specified kind.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_184

LANGUAGE: APIDOC
CODE:
```
GetInputList:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - inputKind (String): Restrict the array to only inputs of the specified kind. Value Restrictions: None. Default Behavior: All kinds included.
  Response Fields:
    - inputs (Array<Object>): Array of inputs.
```

----------------------------------------

TITLE: Get Input Default Settings (OBS WebSocket API)
DESCRIPTION: Gets the default settings for an input kind. This API endpoint has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_190

LANGUAGE: APIDOC
CODE:
```
GetInputDefaultSettings:
  Description: Gets the default settings for an input kind.
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    inputKind:
      Type: String
      Description: Input kind to get the default settings for
      Value Restrictions: None
      Default Behavior: N/A
  Response Fields:
    defaultInputSettings:
      Type: Object
      Description: Object of default settings for the input kind
```

----------------------------------------

TITLE: GetInputPropertiesListPropertyItems
DESCRIPTION: Gets the items of a list property from an input's properties. Note: Use this in cases where an input provides a dynamic, selectable list of items. For example, display capture, where it provides a list of available displays.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_210

LANGUAGE: APIDOC
CODE:
```
GetInputPropertiesListPropertyItems:
  Description: Gets the items of a list property from an input's properties. Note: Use this in cases where an input provides a dynamic, selectable list of items. For example, display capture, where it provides a list of available displays.
  Complexity Rating: 4/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - ?inputName (String): Name of the input [Value Restrictions: None] [Default Behavior: Unknown]
    - ?inputUuid (String): UUID of the input [Value Restrictions: None] [Default Behavior: Unknown]
    - propertyName (String): Name of the list property to get the items of [Value Restrictions: None] [Default Behavior: N/A]
  Response Fields:
    - propertyItems (Array<Object>): Array of items in the list property
```

----------------------------------------

TITLE: RecordFileChanged Event
DESCRIPTION: This event indicates that the record output has started writing to a new file, for example, during a file split. It provides the path to the new recording file. This event was added in v5.5.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_128

LANGUAGE: APIDOC
CODE:
```
Event: RecordFileChanged
Properties:
  - newOutputPath: String (File name that the output has begun writing to)
```

----------------------------------------

TITLE: Example Failure RequestResponse Message (OpCode 7) - obs-websocket
DESCRIPTION: This JSON snippet provides an example of a failed 'RequestResponse' message from obs-websocket. It shows the opcode '7', mirrors the client's request type and ID, indicates failure in 'requestStatus', and includes an error 'comment'.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_17

LANGUAGE: json
CODE:
```
{
  "op": 7,
  "d": {
    "requestType": "SetCurrentProgramScene",
    "requestId": "f819dcf0-89cc-11eb-8f0e-382c4ac93b9c",
    "requestStatus": {
      "result": false,
      "code": 608,
      "comment": "Parameter: sceneName"
    }
  }
}
```

----------------------------------------

TITLE: GetSceneTransitionList
DESCRIPTION: Gets an array of all scene transitions in OBS.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_213

LANGUAGE: APIDOC
CODE:
```
GetSceneTransitionList:
  Description: Gets an array of all scene transitions in OBS.
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Response Fields:
    - currentSceneTransitionName (String): Name of the current scene transition. Can be null
    - currentSceneTransitionUuid (String): UUID of the current scene transition. Can be null
    - currentSceneTransitionKind (String): Kind of the current scene transition. Can be null
    - transitions (Array<Object>): Array of transitions
```

----------------------------------------

TITLE: Get Special Inputs API Documentation
DESCRIPTION: Retrieves the names of all special audio inputs configured in OBS, such as Desktop Audio and Mic/Auxiliary Audio inputs.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_186

LANGUAGE: APIDOC
CODE:
```
GetSpecialInputs:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Response Fields:
    - desktop1 (String): Name of the Desktop Audio input.
    - desktop2 (String): Name of the Desktop Audio 2 input.
    - mic1 (String): Name of the Mic/Auxiliary Audio input.
    - mic2 (String): Name of the Mic/Auxiliary Audio 2 input.
    - mic3 (String): Name of the Mic/Auxiliary Audio 3 input.
    - mic4 (String): Name of the Mic/Auxiliary Audio 4 input.
```

----------------------------------------

TITLE: Get Scene Transition Override (OBS-WebSocket API)
DESCRIPTION: Gets the scene transition overridden for a scene. A transition UUID response field is not currently able to be implemented as of 2024-1-18.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_182

LANGUAGE: APIDOC
CODE:
```
GetSceneSceneTransitionOverride
  Description: Gets the scene transition overridden for a scene.
  Note: A transition UUID response field is not currently able to be implemented as of 2024-1-18.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    ?sceneName: String - Name of the scene (Value Restrictions: None, Default Behavior: Unknown)
    ?sceneUuid: String - UUID of the scene (Value Restrictions: None, Default Behavior: Unknown)
  Response Fields:
    transitionName: String - Name of the overridden scene transition, else `null`
    transitionDuration: Number - Duration of the overridden scene transition, else `null`
```

----------------------------------------

TITLE: Get Input Volume (OBS WebSocket API)
DESCRIPTION: Gets the current volume setting of an input. This API endpoint has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_196

LANGUAGE: APIDOC
CODE:
```
GetInputVolume:
  Description: Gets the current volume setting of an input.
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input to get the volume of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input to get the volume of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
  Response Fields:
    inputVolumeMul:
      Type: Number
      Description: Volume setting in mul
    inputVolumeDb:
      Type: Number
      Description: Volume setting in dB
```

----------------------------------------

TITLE: Get OBS-websocket Version Information
DESCRIPTION: Retrieves data about the current OBS Studio plugin and RPC version, including available requests and supported image formats.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_145

LANGUAGE: APIDOC
CODE:
```
GetVersion:
  Description: Gets data about the current plugin and RPC version.
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Response Fields:
    obsVersion:
      Type: String
      Description: Current OBS Studio version
    obsWebSocketVersion:
      Type: String
      Description: Current obs-websocket version
    rpcVersion:
      Type: Number
      Description: Current latest obs-websocket RPC version
    availableRequests:
      Type: Array<String>
      Description: Array of available RPC requests for the currently negotiated RPC version
    supportedImageFormats:
      Type: Array<String>
      Description: Image formats available in `GetSourceScreenshot` and `SaveSourceScreenshot` requests.
    platform:
      Type: String
      Description: Name of the platform. Usually `windows`, `macos`, or `ubuntu` (linux flavor). Not guaranteed to be any of those
    platformDescription:
      Type: String
      Description: Description of the platform, like `Windows 10 (10.0)`
```

----------------------------------------

TITLE: Get List of Available Outputs (OBS-Websocket API)
DESCRIPTION: Retrieves a list of all available outputs configured in OBS. Each output is returned as an object within an array, providing details about each output.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_258

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 4/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  outputs: Array<Object> - Array of outputs
```

----------------------------------------

TITLE: Get Input Kind List API Documentation
DESCRIPTION: Retrieves an array of all available input kinds that can be created in OBS. The returned list can be unversioned or include version suffixes if available.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_185

LANGUAGE: APIDOC
CODE:
```
GetInputKindList:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - unversioned (Boolean): True == Return all kinds as unversioned, False == Return with version suffixes (if available). Value Restrictions: None. Default Behavior: false.
  Response Fields:
    - inputKinds (Array<String>): Array of input kinds.
```

----------------------------------------

TITLE: OBS-websocket Scenes Requests API
DESCRIPTION: API methods for managing OBS scenes, including listing available scenes, getting and setting the current program or preview scenes, creating, removing, renaming scenes, and managing scene transition overrides.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_140

LANGUAGE: APIDOC
CODE:
```
Scenes Requests:
  GetSceneList()
  GetGroupList()
  GetCurrentProgramScene()
  SetCurrentProgramScene()
  GetCurrentPreviewScene()
  SetCurrentPreviewScene()
  CreateScene()
  RemoveScene()
  SetSceneName()
  GetSceneSceneTransitionOverride()
  SetSceneSceneTransitionOverride()
```

----------------------------------------

TITLE: OBS-websocket Transitions Requests API
DESCRIPTION: API methods for managing OBS scene transitions, including listing transition kinds, getting and setting the current scene transition, adjusting its duration and settings, querying the transition cursor position, triggering studio mode transitions, and setting the T-bar position.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_142

LANGUAGE: APIDOC
CODE:
```
Transitions Requests:
  GetTransitionKindList()
  GetSceneTransitionList()
  GetCurrentSceneTransition()
  SetCurrentSceneTransition()
  SetCurrentSceneTransitionDuration()
  SetCurrentSceneTransitionSettings()
  GetCurrentSceneTransitionCursor()
  TriggerStudioModeTransition()
  SetTBarPosition()
```

----------------------------------------

TITLE: GetMonitorList
DESCRIPTION: Gets a list of connected monitors and information about them.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_288

LANGUAGE: APIDOC
CODE:
```
Response Fields:
  monitors (Array<Object>): a list of detected monitors with some information.
```

----------------------------------------

TITLE: Get Current Scene Transition Cursor
DESCRIPTION: Gets the cursor position of the current scene transition. Note: transitionCursor will return 1.0 when the transition is inactive.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_218

LANGUAGE: APIDOC
CODE:
```
GetCurrentSceneTransitionCursor:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Response Fields:
    transitionCursor: Number - Cursor position, between 0.0 and 1.0.
```

----------------------------------------

TITLE: GetTransitionKindList
DESCRIPTION: Gets an array of all available transition kinds. Similar to `GetInputKindList`

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_212

LANGUAGE: APIDOC
CODE:
```
GetTransitionKindList:
  Description: Gets an array of all available transition kinds. Similar to `GetInputKindList`
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Response Fields:
    - transitionKinds (Array<String>): Array of transition kinds
```

----------------------------------------

TITLE: SceneTransitionStarted Event
DESCRIPTION: Documents the 'SceneTransitionStarted' event, which is emitted when a scene transition begins. It includes the name and UUID of the transition that has started.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_110

LANGUAGE: APIDOC
CODE:
```
Event: SceneTransitionStarted
Description: A scene transition has started.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  transitionName: String - Scene transition name
  transitionUuid: String - Scene transition UUID
```

----------------------------------------

TITLE: GetRecordDirectory
DESCRIPTION: Gets the current directory that the record output is set to.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_168

LANGUAGE: APIDOC
CODE:
```
Method: GetRecordDirectory
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  recordDirectory: String - Output directory
```

----------------------------------------

TITLE: GetStreamServiceSettings
DESCRIPTION: Gets the current stream service settings (stream destination).

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_166

LANGUAGE: APIDOC
CODE:
```
Method: GetStreamServiceSettings
Complexity Rating: 4/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  streamServiceType: String - Stream service type, like rtmp_custom or rtmp_common
  streamServiceSettings: Object - Stream service settings
```

----------------------------------------

TITLE: Get Output Settings API for OBS WebSocket
DESCRIPTION: Retrieves the current settings of a specified OBS output. Requires the output name as input and returns the output settings object.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_263

LANGUAGE: APIDOC
CODE:
```
GetOutputSettings:
  Request:
    outputName: String - Output name
  Response:
    outputSettings: Object - Output settings
```

----------------------------------------

TITLE: SetVideoSettings
DESCRIPTION: Sets the current video settings. Note: Fields must be specified in pairs. For example, you cannot set only baseWidth without needing to specify baseHeight.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_165

LANGUAGE: APIDOC
CODE:
```
Method: SetVideoSettings
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  ?fpsNumerator: Number - Numerator of the fractional FPS value (Value Restrictions: >= 1)
  ?fpsDenominator: Number - Denominator of the fractional FPS value (Value Restrictions: >= 1)
  ?baseWidth: Number - Width of the base (canvas) resolution in pixels (Value Restrictions: >= 1, <= 4096)
  ?baseHeight: Number - Height of the base (canvas) resolution in pixels (Value Restrictions: >= 1, <= 4096)
  ?outputWidth: Number - Width of the output resolution in pixels (Value Restrictions: >= 1, <= 4096)
  ?outputHeight: Number - Height of the output resolution in pixels (Value Restrictions: >= 1, <= 4096)
```

----------------------------------------

TITLE: Get Input Mute State (OBS WebSocket API)
DESCRIPTION: Gets the audio mute state of an input. This API endpoint has a complexity rating of 2/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_193

LANGUAGE: APIDOC
CODE:
```
GetInputMute:
  Description: Gets the audio mute state of an input.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of input to get the mute state of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of input to get the mute state of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
  Response Fields:
    inputMuted:
      Type: Boolean
      Description: Whether the input is muted
```

----------------------------------------

TITLE: GetProfileParameter
DESCRIPTION: Gets a parameter from the current profile's configuration.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_162

LANGUAGE: APIDOC
CODE:
```
Method: GetProfileParameter
Complexity Rating: 4/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  parameterCategory: String - Category of the parameter to get
  parameterName: String - Name of the parameter to get

Response Fields:
  parameterValue: String - Value associated with the parameter. null if not set and no default
  defaultParameterValue: String - Default value associated with the parameter. null if no default
```

----------------------------------------

TITLE: GetInputAudioBalance API Method
DESCRIPTION: Gets the audio balance of a specified input. The balance value ranges from 0.0 to 1.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_198

LANGUAGE: APIDOC
CODE:
```
GetInputAudioBalance:
  Description: Gets the audio balance of an input.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - Name: inputName (Optional)
      Type: String
      Description: Name of the input to get the audio balance of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputUuid (Optional)
      Type: String
      Description: UUID of the input to get the audio balance of
      Value Restrictions: None
      Default Behavior: Unknown
  Response Fields:
    - Name: inputAudioBalance
      Type: Number
      Description: Audio balance value from 0.0-1.0
```

----------------------------------------

TITLE: GetInputAudioSyncOffset API Method
DESCRIPTION: Gets the audio sync offset of an input. The offset can be a negative value.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_200

LANGUAGE: APIDOC
CODE:
```
GetInputAudioSyncOffset:
  Description: Gets the audio sync offset of an input.
  Note: The audio sync offset can be negative too!
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - Name: inputName (Optional)
      Type: String
      Description: Name of the input to get the audio sync offset of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputUuid (Optional)
      Type: String
      Description: UUID of the input to get the audio sync offset of
      Value Restrictions: None
      Default Behavior: Unknown
  Response Fields:
    - Name: inputAudioSyncOffset
      Type: Number
      Description: Audio sync offset in milliseconds
```

----------------------------------------

TITLE: Get Input Audio Tracks API Documentation
DESCRIPTION: Retrieves the enable state of all audio tracks for a specified input. This API endpoint is part of OBS-websocket, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_204

LANGUAGE: APIDOC
CODE:
```
GetInputAudioTracks:
  Description: Gets the enable state of all audio tracks of an input.
  Details:
    Complexity Rating: 2/5
    Latest Supported RPC Version: 1
    Added in: v5.0.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
  Response Fields:
    inputAudioTracks:
      Type: Object
      Description: Object of audio tracks and associated enable states
```

----------------------------------------

TITLE: GetSceneList API Method
DESCRIPTION: Gets an array of all scenes in OBS.

- Complexity Rating: 2/5
- Latest Supported RPC Version: 1
- Added in v5.0.0

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_173

LANGUAGE: APIDOC
CODE:
```
GetSceneList:
  Response Fields:
    currentProgramSceneName: String (Current program scene name. Can be `null` if internal state desync)
    currentProgramSceneUuid: String (Current program scene UUID. Can be `null` if internal state desync)
    currentPreviewSceneName: String (Current preview scene name. `null` if not in studio mode)
    currentPreviewSceneUuid: String (Current preview scene UUID. `null` if not in studio mode)
    scenes: Array<Object> (Array of scenes)
```

----------------------------------------

TITLE: GetProfileList API Method
DESCRIPTION: Gets an array of all available profiles. This method returns the name of the current profile and a list of all existing profiles.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_158

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  - currentProfileName: String - The name of the current profile
  - profiles: Array<String> - Array of all available profiles
```

----------------------------------------

TITLE: OBS-websocket Inputs Requests API
DESCRIPTION: API methods for managing OBS inputs, including listing inputs and their kinds, creating, removing, renaming, getting and setting input settings, controlling mute and volume, adjusting audio balance, sync offset, monitor type, audio tracks, deinterlace mode and field order, and interacting with input properties.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_141

LANGUAGE: APIDOC
CODE:
```
Inputs Requests:
  GetInputList()
  GetInputKindList()
  GetSpecialInputs()
  CreateInput()
  RemoveInput()
  SetInputName()
  GetInputDefaultSettings()
  GetInputSettings()
  SetInputSettings()
  GetInputMute()
  SetInputMute()
  ToggleInputMute()
  GetInputVolume()
  SetInputVolume()
  GetInputAudioBalance()
  SetInputAudioBalance()
  GetInputAudioSyncOffset()
  SetInputAudioSyncOffset()
  GetInputAudioMonitorType()
  SetInputAudioMonitorType()
  GetInputAudioTracks()
  SetInputAudioTracks()
  GetInputDeinterlaceMode()
  SetInputDeinterlaceMode()
  GetInputDeinterlaceFieldOrder()
  SetInputDeinterlaceFieldOrder()
  GetInputPropertiesListPropertyItems()
  PressInputPropertiesButton()
```

----------------------------------------

TITLE: MediaInputPlaybackStarted Event
DESCRIPTION: This event is triggered when a media input begins playing. It provides the name and UUID of the input that started playback. This event was added in v5.0.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_132

LANGUAGE: APIDOC
CODE:
```
Event: MediaInputPlaybackStarted
Properties:
  - inputName: String (Name of the input)
  - inputUuid: String (UUID of the input)
```

----------------------------------------

TITLE: Get OBS-websocket Statistics
DESCRIPTION: Retrieves statistics about OBS, obs-websocket, and the current session, including CPU usage, memory, FPS, and message counts.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_146

LANGUAGE: APIDOC
CODE:
```
GetStats:
  Description: Gets statistics about OBS, obs-websocket, and the current session.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Response Fields:
    cpuUsage:
      Type: Number
      Description: Current CPU usage in percent
    memoryUsage:
      Type: Number
      Description: Amount of memory in MB currently being used by OBS
    availableDiskSpace:
      Type: Number
      Description: Available disk space on the device being used for recording storage
    activeFps:
      Type: Number
      Description: Current FPS being rendered
    averageFrameRenderTime:
      Type: Number
      Description: Average time in milliseconds that OBS is taking to render a frame
    renderSkippedFrames:
      Type: Number
      Description: Number of frames skipped by OBS in the render thread
    renderTotalFrames:
      Type: Number
      Description: Total number of frames outputted by the render thread
    outputSkippedFrames:
      Type: Number
      Description: Number of frames skipped by OBS in the output thread
    outputTotalFrames:
      Type: Number
      Description: Total number of frames outputted by the output thread
    webSocketSessionIncomingMessages:
      Type: Number
      Description: Total number of messages received by obs-websocket from the client
    webSocketSessionOutgoingMessages:
      Type: Number
      Description: Total number of messages sent by obs-websocket to the client
```

----------------------------------------

TITLE: Get Media Input Status API
DESCRIPTION: Retrieves the current status of a specified media input, including its state, duration, and cursor position.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_279

LANGUAGE: APIDOC
CODE:
```
Method: GetMediaInputStatus
Description: Gets the status of a media input.
Media States:
  - OBS_MEDIA_STATE_NONE
  - OBS_MEDIA_STATE_PLAYING
  - OBS_MEDIA_STATE_OPENING
  - OBS_MEDIA_STATE_BUFFERING
  - OBS_MEDIA_STATE_PAUSED
  - OBS_MEDIA_STATE_STOPPED
  - OBS_MEDIA_STATE_ENDED
  - OBS_MEDIA_STATE_ERROR
Details:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
Request Fields:
  ?inputName (String): Name of the media input (Value Restrictions: None, Default Behavior: Unknown)
  ?inputUuid (String): UUID of the media input (Value Restrictions: None, Default Behavior: Unknown)
Response Fields:
  mediaState (String): State of the media input
  mediaDuration (Number): Total duration of the playing media in milliseconds. `null` if not playing
  mediaCursor (Number): Position of the cursor in milliseconds. `null` if not playing
```

----------------------------------------

TITLE: GetSourceActive API Method
DESCRIPTION: Gets the active and show state of a source. Compatible with inputs and scenes.

- Complexity Rating: 2/5
- Latest Supported RPC Version: 1
- Added in v5.0.0

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_170

LANGUAGE: APIDOC
CODE:
```
GetSourceActive:
  Request Fields:
    ?sourceName: String (Name of the source to get the active state of)
      Value Restrictions: None
      Default Behavior: Unknown
    ?sourceUuid: String (UUID of the source to get the active state of)
      Value Restrictions: None
      Default Behavior: Unknown
  Response Fields:
    videoActive: Boolean (Whether the source is showing in Program)
    videoShowing: Boolean (Whether the source is showing in the UI (Preview, Projector, Properties))
```

----------------------------------------

TITLE: RequestStatus::InvalidResourceState Error Code
DESCRIPTION: The state of the resource is invalid. For example, if the resource is blocked from being accessed.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_48

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 604
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: GetInputAudioMonitorType API Method
DESCRIPTION: Gets the audio monitor type of an input. The available types are 'OBS_MONITORING_TYPE_NONE', 'OBS_MONITORING_TYPE_MONITOR_ONLY', and 'OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT'.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_202

LANGUAGE: APIDOC
CODE:
```
GetInputAudioMonitorType:
  Description: Gets the audio monitor type of an input.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Available Monitor Types:
    - OBS_MONITORING_TYPE_NONE
    - OBS_MONITORING_TYPE_MONITOR_ONLY
    - OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
  Request Fields:
    - Name: inputName (Optional)
      Type: String
      Description: Name of the input to get the audio monitor type of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputUuid (Optional)
      Type: String
      Description: UUID of the input to get the audio monitor type of
      Value Restrictions: None
      Default Behavior: Unknown
  Response Fields:
    - Name: monitorType
      Type: String
      Description: Audio monitor type
```

----------------------------------------

TITLE: Create Input API Documentation
DESCRIPTION: Creates a new input in OBS and adds it as a scene item to a specified scene. This method allows for programmatic creation of sources with initial settings and enabled state.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_187

LANGUAGE: APIDOC
CODE:
```
CreateInput:
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - sceneName (String): Name of the scene to add the input to as a scene item. Value Restrictions: None. Default Behavior: Unknown.
    - sceneUuid (String): UUID of the scene to add the input to as a scene item. Value Restrictions: None. Default Behavior: Unknown.
    - inputName (String): Name of the new input to created. Value Restrictions: None. Default Behavior: N/A.
    - inputKind (String): The kind of input to be created. Value Restrictions: None. Default Behavior: N/A.
    - inputSettings (Object): Settings object to initialize the input with. Value Restrictions: None. Default Behavior: Default settings used.
    - sceneItemEnabled (Boolean): Whether to set the created scene item to enabled or disabled. Value Restrictions: None. Default Behavior: True.
  Response Fields:
    - inputUuid (String): UUID of the newly created input.
    - sceneItemId (Number): ID of the newly created scene item.
```

----------------------------------------

TITLE: OBS-WebSocket Hello Message (OpCode 0) API
DESCRIPTION: Detailed API documentation for the 'Hello' message (OpCode 0), the first message sent by the obs-websocket server, including its purpose, sender/receiver, and data keys with their descriptions.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_5

LANGUAGE: APIDOC
CODE:
```
Hello (OpCode 0):
  Sent from: obs-websocket
  Sent to: Freshly connected websocket client
  Description: First message sent from the server immediately on client connection. Contains authentication information if auth is required. Also contains RPC version for version negotiation.
  Data Keys:
    obsStudioVersion: string
    obsWebSocketVersion: string
    rpcVersion: number (current rpc version, increments on each breaking change)
    authentication: object (optional)
      challenge: string
      salt: string
```

----------------------------------------

TITLE: GetSceneCollectionList API Method
DESCRIPTION: Gets an array of all available scene collections. This method provides the name of the current scene collection and a list of all existing scene collections.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_155

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  - currentSceneCollectionName: String - The name of the current scene collection
  - sceneCollections: Array<String> - Array of all available scene collections
```

----------------------------------------

TITLE: OBS-websocket Scene Items Requests API
DESCRIPTION: API methods for managing items within OBS scenes, including listing scene items, getting group scene items, retrieving item IDs and sources, creating, removing, duplicating, and transforming scene items.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_144

LANGUAGE: APIDOC
CODE:
```
Scene Items Requests:
  GetSceneItemList()
  GetGroupSceneItemList()
  GetSceneItemId()
  GetSceneItemSource()
  CreateSceneItem()
  RemoveSceneItem()
  DuplicateSceneItem()
  GetSceneItemTransform()
  SetSceneItemTransform()
```

----------------------------------------

TITLE: GetSourceScreenshot API Method
DESCRIPTION: Gets a Base64-encoded screenshot of a source. The `imageWidth` and `imageHeight` parameters are treated as "scale to inner", meaning the smallest ratio will be used and the aspect ratio of the original resolution is kept. If `imageWidth` and `imageHeight` are not specified, the compressed image will use the full resolution of the source. Compatible with inputs and scenes.

- Complexity Rating: 4/5
- Latest Supported RPC Version: 1
- Added in v5.0.0

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_171

LANGUAGE: APIDOC
CODE:
```
GetSourceScreenshot:
  Request Fields:
    ?sourceName: String (Name of the source to take a screenshot of)
      Value Restrictions: None
      Default Behavior: Unknown
    ?sourceUuid: String (UUID of the source to take a screenshot of)
      Value Restrictions: None
      Default Behavior: Unknown
    imageFormat: String (Image compression format to use. Use `GetVersion` to get compatible image formats)
      Value Restrictions: None
      Default Behavior: N/A
    ?imageWidth: Number (Width to scale the screenshot to)
      Value Restrictions: >= 8, <= 4096
      Default Behavior: Source value is used
    ?imageHeight: Number (Height to scale the screenshot to)
      Value Restrictions: >= 8, <= 4096
      Default Behavior: Source value is used
    ?imageCompressionQuality: Number (Compression quality to use. 0 for high compression, 100 for uncompressed. -1 to use "default" (whatever that means, idk))
      Value Restrictions: >= -1, <= 100
      Default Behavior: -1
  Response Fields:
    imageData: String (Base64-encoded screenshot)
```

----------------------------------------

TITLE: GetHotkeyList API
DESCRIPTION: Gets an array of all hotkey names in OBS. Note: Hotkey functionality in obs-websocket comes as-is, and we do not guarantee support if things are broken. In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_149

LANGUAGE: APIDOC
CODE:
```
GetHotkeyList:
  Description: Gets an array of all hotkey names in OBS. Note: Hotkey functionality in obs-websocket comes as-is, and we do not guarantee support if things are broken. In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests.
  Complexity Rating: 4/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Response Fields:
    hotkeys:
      Type: Array<String>
      Description: Array of hotkey names
```

----------------------------------------

TITLE: Create Scene (OBS-WebSocket API)
DESCRIPTION: Creates a new scene in OBS.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_179

LANGUAGE: APIDOC
CODE:
```
CreateScene
  Description: Creates a new scene in OBS.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    sceneName: String - Name for the new scene (Value Restrictions: None, Default Behavior: N/A)
  Response Fields:
    sceneUuid: String - UUID of the created scene
```

----------------------------------------

TITLE: Get Virtual Camera Status (OBS-Websocket API)
DESCRIPTION: Retrieves the current status of the virtual camera output, indicating whether it is active or not. This is a simple query with a boolean response.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_248

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  outputActive: Boolean - Whether the output is active
```

----------------------------------------

TITLE: OBS-WebSocket API: Hello Message (OpCode 0) Definition
DESCRIPTION: Comprehensive API documentation for the 'Hello' message (OpCode 0), the initial message sent by the obs-websocket server. It details the message's purpose, sender/receiver, and the structure of its data keys including versioning and optional authentication parameters.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_4

LANGUAGE: APIDOC
CODE:
```
Message Type: Hello (OpCode 0)
Sent From: obs-websocket
Sent To: Freshly connected websocket client
Description: First message sent from the server immediately on client connection. Contains authentication information if auth is required. Also contains RPC version for version negotiation.

Data Keys:
  - obsStudioVersion: string
    Description: The version of OBS Studio.
  - obsWebSocketVersion: string
    Description: The version of obs-websocket. May be used as a soft feature level hint.
  - rpcVersion: number
    Description: A version number which gets incremented on each breaking change to the obs-websocket protocol. Its usage in this context is to provide the current rpc version that the server would like to use.
  - authentication: object (optional)
    Description: Contains challenge and salt if authentication is required.
    Properties:
      - challenge: string
        Description: The authentication challenge string.
      - salt: string
        Description: The authentication salt string.
```

----------------------------------------

TITLE: Toggle Virtual Camera Output (OBS-Websocket API)
DESCRIPTION: Toggles the active state of the virtual camera output. This method can be used to start or stop the virtual camera. It returns the new active status.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_249

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  outputActive: Boolean - Whether the output is active
```

----------------------------------------

TITLE: OBS-WebSocket: CurrentProfileChanging Event
DESCRIPTION: This event is triggered when the current OBS profile has started the process of changing. This is an informative event indicating a profile transition is underway.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_86

LANGUAGE: APIDOC
CODE:
```
Event: CurrentProfileChanging
Description: The current profile has begun changing.
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  profileName: String - Name of the current profile
```

----------------------------------------

TITLE: OpenSourceProjector
DESCRIPTION: Opens a projector for a source.

Note: This request serves to provide feature parity with 4.x. It is very likely to be changed/deprecated in a future release.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_290

LANGUAGE: APIDOC
CODE:
```
Request Fields:
  sourceName (String, optional): Name of the source to open a projector for.
  sourceUuid (String, optional): UUID of the source to open a projector for.
  monitorIndex (Number, optional): Monitor index, use `GetMonitorList` to obtain index. Default: -1: Opens projector in windowed mode.
  projectorGeometry (String, optional): Size/Position data for a windowed projector, in Qt Base64 encoded format. Mutually exclusive with `monitorIndex`.
```

----------------------------------------

TITLE: Get Source Filter Information API
DESCRIPTION: Retrieves detailed information for a specific source filter. This includes its enabled state, index position, kind, and associated settings. The source can be identified by name or UUID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_227

LANGUAGE: APIDOC
CODE:
```
GetSourceFilter:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    ?sourceName: String - Name of the source
    ?sourceUuid: String - UUID of the source
    filterName: String - Name of the filter
  Response Fields:
    filterEnabled: Boolean - Whether the filter is enabled
    filterIndex: Number - Index of the filter in the list, beginning at 0
    filterKind: String - The kind of filter
    filterSettings: Object - Settings object associated with the filter
```

----------------------------------------

TITLE: OBS-Websocket API: ObsOutputState Enum
DESCRIPTION: Defines the various states an OBS output can be in, from unknown to started, stopped, and reconnecting. These states provide information about the current status of streaming or recording outputs.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_79

LANGUAGE: APIDOC
CODE:
```
ObsOutputState:
  OBS_WEBSOCKET_OUTPUT_UNKNOWN:
    Description: Unknown state.
    Identifier Value: OBS_WEBSOCKET_OUTPUT_UNKNOWN
    Latest Supported RPC Version: 1
    Added in: v5.0.0
  OBS_WEBSOCKET_OUTPUT_STARTING:
    Description: The output is starting.
    Identifier Value: OBS_WEBSOCKET_OUTPUT_STARTING
    Latest Supported RPC Version: 1
    Added in: v5.0.0
  OBS_WEBSOCKET_OUTPUT_STARTED:
    Description: The input has started.
    Identifier Value: OBS_WEBSOCKET_OUTPUT_STARTED
    Latest Supported RPC Version: 1
    Added in: v5.0.0
  OBS_WEBSOCKET_OUTPUT_STOPPING:
    Description: The output is stopping.
    Identifier Value: OBS_WEBSOCKET_OUTPUT_STOPPING
    Latest Supported RPC Version: 1
    Added in: v5.0.0
  OBS_WEBSOCKET_OUTPUT_STOPPED:
    Description: The output has stopped.
    Identifier Value: OBS_WEBSOCKET_OUTPUT_STOPPED
    Latest Supported RPC Version: 1
    Added in: v5.0.0
  OBS_WEBSOCKET_OUTPUT_RECONNECTING:
    Description: The output has disconnected and is reconnecting.
    Identifier Value: OBS_WEBSOCKET_OUTPUT_RECONNECTING
    Latest Supported RPC Version: 1
    Added in: v5.0.0
  OBS_WEBSOCKET_OUTPUT_RECONNECTED:
    Description: The output has reconnected successfully.
    Identifier Value: OBS_WEBSOCKET_OUTPUT_RECONNECTED
    Latest Supported RPC Version: 1
    Added in: v5.1.0
  OBS_WEBSOCKET_OUTPUT_PAUSED:
    Description: The output is now paused.
    Identifier Value: OBS_WEBSOCKET_OUTPUT_PAUSED
    Latest Supported RPC Version: 1
    Added in: v5.1.0
  OBS_WEBSOCKET_OUTPUT_RESUMED:
    Description: The output has been resumed (unpaused).
    Identifier Value: OBS_WEBSOCKET_OUTPUT_RESUMED
    Latest Supported RPC Version: 1
    Added in: v5.0.0
```

----------------------------------------

TITLE: Define OBS-Websocket Library and Dependencies
DESCRIPTION: This snippet defines the `obs-websocket` module library, sets up an alias, and ensures the Asio library is found as a required dependency for the project.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_1

LANGUAGE: CMake
CODE:
```
find_package(Asio 1.12.1 REQUIRED)

add_library(obs-websocket MODULE)
add_library(OBS::websocket ALIAS obs-websocket)
```

----------------------------------------

TITLE: Get Scene Item List API
DESCRIPTION: Retrieves a list of all scene items present within a specified scene. This method is specifically designed for standard scenes. The scene can be identified by its name or UUID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_231

LANGUAGE: APIDOC
CODE:
```
GetSceneItemList:
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    ?sceneName: String - Name of the scene to get the items of
    ?sceneUuid: String - UUID of the scene to get the items of
  Response Fields:
    sceneItems: Array<Object> - Array of scene items in the scene
```

----------------------------------------

TITLE: Get Replay Buffer Status (OBS-Websocket API)
DESCRIPTION: Retrieves the current status of the replay buffer output, indicating whether it is active. This is a simple query with a boolean response.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_252

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  outputActive: Boolean - Whether the output is active
```

----------------------------------------

TITLE: Configure Generated Header and Compile Definitions
DESCRIPTION: Configures a generated header file (`plugin-macros.generated.h`) from a template and defines compile-time macros for the `obs-websocket` target, including `ASIO_STANDALONE`, `PLUGIN_TESTS` (if enabled), and Windows-specific `_WEBSOCKETPP_CPP11_STL_` and `_WIN32_WINNT`.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_7

LANGUAGE: CMake
CODE:
```
configure_file(src/plugin-macros.h.in plugin-macros.generated.h)
target_sources(obs-websocket PRIVATE plugin-macros.generated.h)

target_compile_definitions(
  obs-websocket PRIVATE ASIO_STANDALONE $<$<BOOL:${PLUGIN_TESTS}>:PLUGIN_TESTS>
                        $<$<PLATFORM_ID:Windows>:_WEBSOCKETPP_CPP11_STL_> $<$<PLATFORM_ID:Windows>:_WIN32_WINNT=0x0603>)
```

----------------------------------------

TITLE: obs-websocket Connection Protocol Steps
DESCRIPTION: Details the precise sequence of messages exchanged between a client and the obs-websocket server to establish and authenticate a connection. It covers initial HTTP WebSocket upgrade, subprotocol negotiation (JSON or MessagePack), server's 'Hello' message, client's 'Identify' response (with or without authentication), and server's 'Identified' confirmation, including error conditions and reidentification.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_0

LANGUAGE: APIDOC
CODE:
```
Connection Steps:
1. Client initiates HTTP WebSocket upgrade request.
   - Header: Sec-WebSocket-Protocol (optional, default: obswebsocket.json)
     - obswebsocket.json: JSON over text frames
     - obswebsocket.msgpack: MsgPack over binary frames
2. Server sends OpCode 0 Hello message to client.
3. Client listens for Hello, responds with OpCode 1 Identify.
   - If Hello.authentication exists:
     - Client must send Identify with correct authentication string.
     - Failure: Connection closed with WebSocketCloseCode::AuthenticationFailed.
   - If Hello.authentication does not exist:
     - Client sends Identify without authentication string.
   - Client determines server's rpcVersion support:
     - If unsupported: Client provides closest supported version in Identify.
     - Failure: Connection closed with WebSocketCloseCode::UnsupportedRpcVersion.
   - Malformed parameters (e.g., invalid type): Connection closed with appropriate close code.
4. Server processes Identify, responds with OpCode 2 Identified.
5. Client begins receiving events and can make requests.
6. Client may send OpCode 3 Reidentify at any time to update session parameters.
   - Server responds as during initial identification.
```

----------------------------------------

TITLE: OBS-websocket Filters Requests API
DESCRIPTION: API methods for managing source filters in OBS, including listing filter kinds, getting filter lists, retrieving default settings, creating, removing, renaming, reordering, setting filter settings, and enabling or disabling filters.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_143

LANGUAGE: APIDOC
CODE:
```
Filters Requests:
  GetSourceFilterKindList()
  GetSourceFilterList()
  GetSourceFilterDefaultSettings()
  CreateSourceFilter()
  RemoveSourceFilter()
  SetSourceFilterName()
  GetSourceFilter()
  SetSourceFilterIndex()
  SetSourceFilterSettings()
  SetSourceFilterEnabled()
```

----------------------------------------

TITLE: CreateProfile API Method
DESCRIPTION: Creates a new profile and immediately switches to it. This method facilitates the creation and activation of a new OBS profile.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_160

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  - profileName: String - Name for the new profile
```

----------------------------------------

TITLE: Toggle Replay Buffer Output (OBS-Websocket API)
DESCRIPTION: Toggles the active state of the replay buffer output. This method can be used to start or stop the replay buffer. It returns the new active status.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_253

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  outputActive: Boolean - Whether the output is active
```

----------------------------------------

TITLE: Get Record Status API
DESCRIPTION: Retrieves the current status of the OBS record output, including its active state, pause status, timecode, duration, and bytes sent.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_270

LANGUAGE: APIDOC
CODE:
```
Method: GetRecordStatus
Description: Gets the status of the record output.
Details:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
Response Fields:
  outputActive (Boolean): Whether the output is active
  outputPaused (Boolean): Whether the output is paused
  outputTimecode (String): Current formatted timecode string for the output
  outputDuration (Number): Current duration in milliseconds for the output
  outputBytes (Number): Number of bytes sent by the output
```

----------------------------------------

TITLE: Get Last Replay Buffer Save File (OBS-Websocket API)
DESCRIPTION: Retrieves the file path of the most recently saved replay buffer recording. This is useful for locating the saved replay.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_257

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Response Fields:
  savedReplayPath: String - File path
```

----------------------------------------

TITLE: GetGroupList API Method
DESCRIPTION: Gets an array of all groups in OBS.

Groups in OBS are actually scenes, but renamed and modified. In obs-websocket, we treat them as scenes where we can.

- Complexity Rating: 2/5
- Latest Supported RPC Version: 1
- Added in v5.0.0

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_174

LANGUAGE: APIDOC
CODE:
```
GetGroupList:
  Response Fields:
    groups: Array<String> (Array of group names)
```

----------------------------------------

TITLE: obs-websocket 5.x.x Protocol: Connection and Identification Flow
DESCRIPTION: Describes the detailed, step-by-step process for a client to connect to and identify with the obs-websocket server, including WebSocket subprotocol negotiation, initial 'Hello' message, client 'Identify' response with optional authentication, and server 'Identified' confirmation. It also covers error handling during the identification phase and the 'Reidentify' mechanism.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_0

LANGUAGE: APIDOC
CODE:
```
Connection Flow:
  1. Initial HTTP Request:
    - Purpose: Establish WebSocket connection.
    - Header: Sec-WebSocket-Protocol
      - Purpose: Specify message encoding.
      - Default: JSON over text.
      - Available Subprotocols:
        - obswebsocket.json: JSON over text frames
        - obswebsocket.msgpack: MsgPack over binary frames

  2. Server Sends Hello (OpCode 0):
    - Trigger: Immediately after WebSocket upgrade.
    - Purpose: Initiate handshake, provide server capabilities.
    - Message Content (implied from text):
      - authentication: (Optional) Object containing challenge for client authentication.
      - rpcVersion: Server's supported RPC protocol version.

  3. Client Sends Identify (OpCode 1):
    - Trigger: After receiving Hello message.
    - Purpose: Respond to server, provide client parameters, authenticate if required.
    - Message Content (implied from text):
      - authentication: (Optional) Client-generated authentication string (if server required).
      - rpcVersion: Client's closest supported RPC version (negotiated with server's rpcVersion).
      - sessionParameters: (Other parameters as appropriate for session)

    - Authentication Logic:
      - If Hello message contains 'authentication' field: Client must follow 'Creating an authentication string' steps.
      - If Hello message does NOT contain 'authentication' field: Client's Identify message does not require 'authentication' string.

  4. Server Processes Identify:
    - Authentication Validation:
      - If required and missing/incorrect: Connection closed with WebSocketCloseCode::AuthenticationFailed.
    - RPC Version Negotiation:
      - If client's rpcVersion is unsupported: Connection closed with WebSocketCloseCode::UnsupportedRpcVersion.
    - Parameter Validation:
      - If any parameters are malformed: Connection closed with appropriate close code.

  5. Server Sends Identified (OpCode 2):
    - Trigger: After successful processing of client's Identify message.
    - Purpose: Confirm successful identification.
    - Message Content: (No specific fields mentioned, indicates success)

  6. Post-Identification:
    - Client begins receiving events.
    - Client may now make requests.

  7. Client Sends Reidentify (OpCode 3):
    - Trigger: Any time after initial identification.
    - Purpose: Update certain allowed session parameters.
    - Message Content: Similar to Identify message, containing updated session parameters.
    - Server Response: Same as during initial identification.
```

----------------------------------------

TITLE: Request (OpCode 6)
DESCRIPTION: This message is sent from an identified client to obs-websocket when the client is making a request, such as getting the current scene or creating a source. It includes the `requestType` to specify the action, a unique `requestId` for tracking, and optional `requestData` relevant to the request.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_11

LANGUAGE: txt
CODE:
```
{
  "requestType": string,
  "requestId": string,
  "requestData": object(optional),

}
```

LANGUAGE: json
CODE:
```
{
  "op": 6,
  "d": {
    "requestType": "SetCurrentProgramScene",
    "requestId": "f819dcf0-89cc-11eb-8f0e-382c4ac93b9c",
    "requestData": {
      "sceneName": "Scene 12"
    }
  }
}
```

----------------------------------------

TITLE: RequestStatus::ResourceNotConfigurable Error Code
DESCRIPTION: The resource does not support being configured. This is particularly relevant to transitions, where they do not always have changeable settings.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_50

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 606
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Get Input Deinterlace Mode API Documentation
DESCRIPTION: Retrieves the deinterlace mode of an input. Deinterlacing functionality is restricted to async inputs only. This API endpoint is part of OBS-websocket, supports RPC Version 1, and was added in v5.6.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_206

LANGUAGE: APIDOC
CODE:
```
GetInputDeinterlaceMode:
  Description: Gets the deinterlace mode of an input.
  Details:
    Deinterlace Modes:
      - OBS_DEINTERLACE_MODE_DISABLE
      - OBS_DEINTERLACE_MODE_DISCARD
      - OBS_DEINTERLACE_MODE_RETRO
      - OBS_DEINTERLACE_MODE_BLEND
      - OBS_DEINTERLACE_MODE_BLEND_2X
      - OBS_DEINTERLACE_MODE_LINEAR
      - OBS_DEINTERLACE_MODE_LINEAR_2X
      - OBS_DEINTERLACE_MODE_YADIF
      - OBS_DEINTERLACE_MODE_YADIF_2X
    Notes: Deinterlacing functionality is restricted to async inputs only.
    Complexity Rating: 2/5
    Latest Supported RPC Version: 1
    Added in: v5.6.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
  Response Fields:
    inputDeinterlaceMode:
      Type: String
      Description: Deinterlace mode of the input
```

----------------------------------------

TITLE: Add Utility Component Source Files
DESCRIPTION: Adds various utility source files for compatibility, cryptography, JSON handling, OBS-specific helpers (actions, arrays, numbers, objects, search, strings, volume meters), and platform-specific functionalities.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_6

LANGUAGE: CMake
CODE:
```
target_sources(
  obs-websocket
  PRIVATE # cmake-format: sortable
          src/utils/Compat.cpp
          src/utils/Compat.h
          src/utils/Crypto.cpp
          src/utils/Crypto.h
          src/utils/Json.cpp
          src/utils/Json.h
          src/utils/Obs.cpp
          src/utils/Obs.h
          src/utils/Obs_ActionHelper.cpp
          src/utils/Obs_ArrayHelper.cpp
          src/utils/Obs_NumberHelper.cpp
          src/utils/Obs_ObjectHelper.cpp
          src/utils/Obs_SearchHelper.cpp
          src/utils/Obs_StringHelper.cpp
          src/utils/Obs_VolumeMeter.cpp
          src/utils/Obs_VolumeMeter.h
          src/utils/Obs_VolumeMeter_Helpers.h
          src/utils/Platform.cpp
          src/utils/Platform.h
          src/utils/Utils.h)
```

----------------------------------------

TITLE: RequestStatus::NotEnoughResources Error Code
DESCRIPTION: There are not enough instances of the resource in order to perform the request.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_47

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 603
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: PressInputPropertiesButton
DESCRIPTION: Presses a button in the properties of an input. Some known `propertyName` values are: `refreshnocache` - Browser source reload button. Note: Use this in cases where there is a button in the properties of an input that cannot be accessed in any other way. For example, browser sources, where there is a refresh button.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_211

LANGUAGE: APIDOC
CODE:
```
PressInputPropertiesButton:
  Description: Presses a button in the properties of an input. Some known `propertyName` values are: `refreshnocache` - Browser source reload button. Note: Use this in cases where there is a button in the properties of an input that cannot be accessed in any other way. For example, browser sources, where there is a refresh button.
  Complexity Rating: 4/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - ?inputName (String): Name of the input [Value Restrictions: None] [Default Behavior: Unknown]
    - ?inputUuid (String): UUID of the input [Value Restrictions: None] [Default Behavior: Unknown]
    - propertyName (String): Name of the button property to press [Value Restrictions: None] [Default Behavior: N/A]
```

----------------------------------------

TITLE: Get Stream Status API for OBS WebSocket
DESCRIPTION: Retrieves the current status of the OBS stream output, including its activity, reconnection status, timecode, duration, congestion, bytes sent, and frame statistics.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_265

LANGUAGE: APIDOC
CODE:
```
GetStreamStatus:
  Request: None
  Response:
    outputActive: Boolean - Whether the output is active
    outputReconnecting: Boolean - Whether the output is currently reconnecting
    outputTimecode: String - Current formatted timecode string for the output
    outputDuration: Number - Current duration in milliseconds for the output
    outputCongestion: Number - Congestion of the output
    outputBytes: Number - Number of bytes sent by the output
    outputSkippedFrames: Number - Number of frames skipped by the output's process
    outputTotalFrames: Number - Total number of frames delivered by the output's process
```

----------------------------------------

TITLE: Get Output Status API for OBS WebSocket
DESCRIPTION: Retrieves the current status of a specified OBS output, including its activity, reconnection status, timecode, duration, congestion, bytes sent, and frame statistics. Requires the output name as input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_259

LANGUAGE: APIDOC
CODE:
```
GetOutputStatus:
  Request:
    outputName: String - Output name
  Response:
    outputActive: Boolean - Whether the output is active
    outputReconnecting: Boolean - Whether the output is reconnecting
    outputTimecode: String - Current formatted timecode string for the output
    outputDuration: Number - Current duration in milliseconds for the output
    outputCongestion: Number - Congestion of the output
    outputBytes: Number - Number of bytes sent by the output
    outputSkippedFrames: Number - Number of frames skipped by the output's process
    outputTotalFrames: Number - Total number of frames delivered by the output's process
```

----------------------------------------

TITLE: Add WebSocket Server Component Source Files
DESCRIPTION: Includes source files related to the WebSocket server implementation, covering RPC sessions, close codes, opcodes, and the core server protocol.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_3

LANGUAGE: CMake
CODE:
```
target_sources(
  obs-websocket
  PRIVATE # cmake-format: sortable
          src/websocketserver/rpc/WebSocketSession.h
          src/websocketserver/types/WebSocketCloseCode.h
          src/websocketserver/types/WebSocketOpCode.h
          src/websocketserver/WebSocketServer.cpp
          src/websocketserver/WebSocketServer.h
          src/websocketserver/WebSocketServer_Protocol.cpp)
```

----------------------------------------

TITLE: Get Input Deinterlace Field Order API Documentation
DESCRIPTION: Retrieves the deinterlace field order of an input. Deinterlacing functionality is restricted to async inputs only. This API endpoint is part of OBS-websocket, supports RPC Version 1, and was added in v5.6.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_208

LANGUAGE: APIDOC
CODE:
```
GetInputDeinterlaceFieldOrder:
  Description: Gets the deinterlace field order of an input.
  Details:
    Deinterlace Field Orders:
      - OBS_DEINTERLACE_FIELD_ORDER_TOP
      - OBS_DEINTERLACE_FIELD_ORDER_BOTTOM
    Notes: Deinterlacing functionality is restricted to async inputs only.
    Complexity Rating: 2/5
    Latest Supported RPC Version: 1
    Added in: v5.6.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
  Response Fields:
    inputDeinterlaceFieldOrder:
      Type: String
      Description: Deinterlace field order of the input
```

----------------------------------------

TITLE: GetPersistentData API Method
DESCRIPTION: Gets the value of a "slot" from the selected persistent data realm. This method allows retrieval of stored data based on a specified realm (global or profile) and slot name.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_153

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  - realm: String - The data realm to select. OBS_WEBSOCKET_DATA_REALM_GLOBAL or OBS_WEBSOCKET_DATA_REALM_PROFILE
  - slotName: String - The name of the slot to retrieve data from

Response Fields:
  - slotValue: Any - Value associated with the slot. null if not set
```

----------------------------------------

TITLE: Setting Target Properties
DESCRIPTION: Applies various properties to the `obs-websocket` target using a custom `set_target_properties_obs` macro/function. This includes setting the output folder, prefix, and enabling CMake's automatic handling for Qt components (MOC, UIC, RCC).

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_12

LANGUAGE: CMake
CODE:
```
set_target_properties_obs(
  obs-websocket
  PROPERTIES FOLDER plugins
             PREFIX ""
             AUTOMOC ON
             AUTOUIC ON
             AUTORCC ON)
```

----------------------------------------

TITLE: Add Request Handler Component Source Files
DESCRIPTION: Includes source files for handling various requests, including batch requests, and specific handlers for configuration, filters, general, inputs, media inputs, outputs, record, scene items, scenes, sources, stream, transitions, and UI, along with RPC request/result types.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_5

LANGUAGE: CMake
CODE:
```
target_sources(
  obs-websocket
  PRIVATE # cmake-format: sortable
          src/requesthandler/RequestBatchHandler.cpp
          src/requesthandler/RequestBatchHandler.h
          src/requesthandler/RequestHandler.cpp
          src/requesthandler/RequestHandler.h
          src/requesthandler/RequestHandler_Config.cpp
          src/requesthandler/RequestHandler_Filters.cpp
          src/requesthandler/RequestHandler_General.cpp
          src/requesthandler/RequestHandler_Inputs.cpp
          src/requesthandler/RequestHandler_MediaInputs.cpp
          src/requesthandler/RequestHandler_Outputs.cpp
          src/requesthandler/RequestHandler_Record.cpp
          src/requesthandler/RequestHandler_SceneItems.cpp
          src/requesthandler/RequestHandler_Scenes.cpp
          src/requesthandler/RequestHandler_Sources.cpp
          src/requesthandler/RequestHandler_Stream.cpp
          src/requesthandler/RequestHandler_Transitions.cpp
          src/requesthandler/RequestHandler_Ui.cpp
          src/requesthandler/rpc/Request.cpp
          src/requesthandler/rpc/Request.h
          src/requesthandler/rpc/RequestBatchRequest.cpp
          src/requesthandler/rpc/RequestBatchRequest.h
          src/requesthandler/rpc/RequestResult.cpp
          src/requesthandler/rpc/RequestResult.h
          src/requesthandler/types/RequestBatchExecutionType.h
          src/requesthandler/types/RequestStatus.h)
```

----------------------------------------

TITLE: Get Scene Item Blend Mode (OBS-Websocket API)
DESCRIPTION: Retrieves the current blend mode of a specified scene item. This API call requires either a scene name or UUID, along with the scene item's numeric ID. It returns the current blend mode as a string.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_246

LANGUAGE: APIDOC
CODE:
```
Blend modes:
  - OBS_BLEND_NORMAL
  - OBS_BLEND_ADDITIVE
  - OBS_BLEND_SUBTRACT
  - OBS_BLEND_SCREEN
  - OBS_BLEND_MULTIPLY
  - OBS_BLEND_LIGHTEN
  - OBS_BLEND_DARKEN

Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  ?sceneName: String - Name of the scene the item is in (Value Restrictions: None, Default Behavior: Unknown)
  ?sceneUuid: String - UUID of the scene the item is in (Value Restrictions: None, Default Behavior: Unknown)
  sceneItemId: Number - Numeric ID of the scene item (Value Restrictions: >= 0, Default Behavior: N/A)

Response Fields:
  sceneItemBlendMode: String - Current blend mode
```

----------------------------------------

TITLE: Define obs-websocket Event Documentation Format
DESCRIPTION: Outlines the JSDoc-like comment structure for documenting events in obs-websocket, detailing tags for data fields, event type, subscription requirements, complexity, RPC version, initial version, and category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/README.md#_snippet_2

LANGUAGE: JavaScript
CODE:
```
/**
 * [description]
 *
 * @dataField [field name] | [value type] | [field description]
 * [... more @dataField entries ...]
 *
 * @eventType [type]
 * @eventSubscription [EventSubscription requirement]
 * @complexity [complexity rating, 1-5]
 * @rpcVersion [latest available RPC version, use `-1` unless deprecated.]
 * @initialVersion [first obs-websocket version this is found in]
 * @category [event category]
 * @api events
 */
```

----------------------------------------

TITLE: Get Group Scene Item List API
DESCRIPTION: Retrieves a list of scene items within a specified group. Note that using groups in OBS is discouraged due to underlying issues; nested scenes are recommended as an alternative. The group can be identified by its name or UUID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_232

LANGUAGE: APIDOC
CODE:
```
GetGroupSceneItemList:
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    ?sceneName: String - Name of the group to get the items of
    ?sceneUuid: String - UUID of the group to get the items of
  Response Fields:
    sceneItems: Array<Object> - Array of scene items in the group
```

----------------------------------------

TITLE: CreateSceneItem API Reference
DESCRIPTION: Creates a new scene item in a specified scene using an existing source. Allows for initial enabling/disabling of the new item.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_235

LANGUAGE: APIDOC
CODE:
```
CreateSceneItem:
  Request Fields:
    ?sceneName: String - Name of the scene to create the new item in
    ?sceneUuid: String - UUID of the scene to create the new item in
    ?sourceName: String - Name of the source to add to the scene
    ?sourceUuid: String - UUID of the source to add to the scene
    ?sceneItemEnabled: Boolean - Enable state to apply to the scene item on creation
  Response Fields:
    sceneItemId: Number - Numeric ID of the scene item
```

----------------------------------------

TITLE: OBS-websocket Configuration Requests API
DESCRIPTION: API methods for managing OBS configuration settings, such as persistent data, scene collections, profiles, video settings, stream service settings, and the recording directory.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_138

LANGUAGE: APIDOC
CODE:
```
Config Requests:
  GetPersistentData()
  SetPersistentData()
  GetSceneCollectionList()
  SetCurrentSceneCollection()
  CreateSceneCollection()
  GetProfileList()
  SetCurrentProfile()
  CreateProfile()
  RemoveProfile()
  GetProfileParameter()
  SetProfileParameter()
  GetVideoSettings()
  SetVideoSettings()
  GetStreamServiceSettings()
  SetStreamServiceSettings()
  GetRecordDirectory()
  SetRecordDirectory()
```

----------------------------------------

TITLE: Configure OBS-Websocket Project with CMake
DESCRIPTION: This CMake script configures the OBS-Websocket project. It sets minimum CMake version requirements, defines project versions, includes an API definition, enables or disables the websocket plugin based on an option, and locates essential dependencies such as Qt6, nlohmann JSON, qrcodegencpp, and WebSocket++.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_0

LANGUAGE: CMake
CODE:
```
cmake_minimum_required(VERSION 3.28...3.30)

set(obs-websocket_VERSION 5.6.1)
set(OBS_WEBSOCKET_RPC_VERSION 1)

include(cmake/obs-websocket-api.cmake)

option(ENABLE_WEBSOCKET "Enable building OBS with websocket plugin" ON)
if(NOT ENABLE_WEBSOCKET)
  target_disable(obs-websocket)
  return()
endif()

# Find Qt
find_package(Qt6 REQUIRED Core Widgets Svg Network)

# Find nlohmann JSON
find_package(nlohmann_json 3.11 REQUIRED)

# Find qrcodegencpp
set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)
find_package(qrcodegencpp REQUIRED)
set(CMAKE_FIND_PACKAGE_PREFER_CONFIG OFF)

# Find WebSocket++
find_package(Websocketpp 0.8 REQUIRED)
```

----------------------------------------

TITLE: OpenVideoMixProjector
DESCRIPTION: Opens a projector for a specific output video mix.

Mix types:
- `OBS_WEBSOCKET_VIDEO_MIX_TYPE_PREVIEW`
- `OBS_WEBSOCKET_VIDEO_MIX_TYPE_PROGRAM`
- `OBS_WEBSOCKET_VIDEO_MIX_TYPE_MULTIVIEW`

Note: This request serves to provide feature parity with 4.x. It is very likely to be changed/deprecated in a future release.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_289

LANGUAGE: APIDOC
CODE:
```
Request Fields:
  videoMixType (String): Type of mix to open.
  monitorIndex (Number, optional): Monitor index, use `GetMonitorList` to obtain index. Default: -1: Opens projector in windowed mode.
  projectorGeometry (String, optional): Size/Position data for a windowed projector, in Qt Base64 encoded format. Mutually exclusive with `monitorIndex`.
```

----------------------------------------

TITLE: Set Input Settings (OBS WebSocket API)
DESCRIPTION: Sets the settings of an input. This API endpoint has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_192

LANGUAGE: APIDOC
CODE:
```
SetInputSettings:
  Description: Sets the settings of an input.
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input to set the settings of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input to set the settings of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputSettings:
      Type: Object
      Description: Object of settings to apply
      Value Restrictions: None
      Default Behavior: N/A
    overlay:
      Type: Boolean
      Description: True == apply the settings on top of existing ones, False == reset the input to its defaults, then apply settings.
      Value Restrictions: None
      Default Behavior: true
      Optional: true
```

----------------------------------------

TITLE: RequestStatus::ResourceCreationFailed Error Code
DESCRIPTION: Creating the resource failed.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_52

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 700
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Identify (OpCode 1)
DESCRIPTION: Response to `Hello` message, should contain authentication string if authentication is required, along with PubSub subscriptions and other session parameters.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_8

LANGUAGE: APIDOC
CODE:
```
Sent from: Freshly connected websocket client
Sent to: obs-websocket

Data Keys:
{
  "rpcVersion": number,
  "authentication": string(optional),
  "eventSubscriptions": number(optional) = (EventSubscription::All)
}
  rpcVersion: The version number that the client would like the obs-websocket server to use.
  eventSubscriptions: A bitmask of `EventSubscriptions` items to subscribe to events and event categories at will. By default, all event categories are subscribed, except for events marked as high volume. High volume events must be explicitly subscribed to.

Example Message:
{
  "op": 1,
  "d": {
    "rpcVersion": 1,
    "authentication": "Dj6cLS+jrNA0HpCArRg0Z/Fc+YHdt2FQfAvgD1mip6Y=",
    "eventSubscriptions": 33
  }
}
```

----------------------------------------

TITLE: Set Current Scene Transition Settings
DESCRIPTION: Sets the settings of the current scene transition. This method allows applying new settings to the active transition, with an option to overlay or replace existing settings.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_217

LANGUAGE: APIDOC
CODE:
```
SetCurrentSceneTransitionSettings:
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    transitionSettings: Object - Settings object to apply to the transition. Can be {}.
    overlay: Boolean - Whether to overlay over the current settings or replace them (Optional, Default: true).
```

----------------------------------------

TITLE: Set Output Settings API for OBS WebSocket
DESCRIPTION: Configures the settings for a specified OBS output. Requires the output name and a new output settings object as inputs.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_264

LANGUAGE: APIDOC
CODE:
```
SetOutputSettings:
  Request:
    outputName: String - Output name
    outputSettings: Object - Output settings
  Response: None
```

----------------------------------------

TITLE: Set Current Preview Scene (OBS-WebSocket API)
DESCRIPTION: Sets the current preview scene. Only available when studio mode is enabled.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_178

LANGUAGE: APIDOC
CODE:
```
SetCurrentPreviewScene
  Description: Sets the current preview scene.
  Note: Only available when studio mode is enabled.
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    ?sceneName: String - Scene name to set as the current preview scene (Value Restrictions: None, Default Behavior: Unknown)
    ?sceneUuid: String - Scene UUID to set as the current preview scene (Value Restrictions: None, Default Behavior: Unknown)
```

----------------------------------------

TITLE: Add Core OBS-Websocket Source Files
DESCRIPTION: Adds the primary C++ source and header files for the `obs-websocket` module, including configuration, UI forms, and the main WebSocket API implementation.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_2

LANGUAGE: CMake
CODE:
```
target_sources(
  obs-websocket
  PRIVATE # cmake-format: sortable
          src/Config.cpp
          src/Config.h
          src/forms/ConnectInfo.cpp
          src/forms/ConnectInfo.h
          src/forms/resources.qrc
          src/forms/SettingsDialog.cpp
          src/forms/SettingsDialog.h
          src/obs-websocket.cpp
          src/obs-websocket.h
          src/WebSocketApi.cpp
          src/WebSocketApi.h)
```

----------------------------------------

TITLE: Set OBS-Websocket Compile Options
DESCRIPTION: Applies specific compile options to the `obs-websocket` target, including suppressing Windows warnings (`/wd4267`, `/wd4996`) and enabling `-Wall` for GNU/Clang compilers while suppressing specific warnings like `float-conversion`, `shadow`, `format-overflow`, `int-conversion`, `comment`, `deprecated-declarations`, and `null-pointer-subtraction`.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_8

LANGUAGE: CMake
CODE:
```
target_compile_options(
  obs-websocket
  PRIVATE $<$<PLATFORM_ID:Windows>:/wd4267>
          $<$<PLATFORM_ID:Windows>:/wd4996>
          $<$<COMPILE_LANG_AND_ID:CXX,GNU,AppleClang,Clang>:-Wall>
          $<$<COMPILE_LANG_AND_ID:CXX,GNU,AppleClang,Clang>:-Wno-error=float-conversion>
          $<$<COMPILE_LANG_AND_ID:CXX,GNU,AppleClang,Clang>:-Wno-error=shadow>
          $<$<COMPILE_LANG_AND_ID:CXX,GNU>:-Wno-error=format-overflow>
          $<$<COMPILE_LANG_AND_ID:CXX,GNU>:-Wno-error=int-conversion>
          $<$<COMPILE_LANG_AND_ID:CXX,GNU>:-Wno-error=comment>
          $<$<COMPILE_LANG_AND_ID:CXX,GNU>:-Wno-error=deprecated-declarations>
          $<$<COMPILE_LANG_AND_ID:CXX,AppleClang,Clang>:-Wno-error=null-pointer-subtraction>)
```

----------------------------------------

TITLE: RequestStatus::ResourceAlreadyExists Error Code
DESCRIPTION: The resource already exists.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_45

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 601
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Trigger Studio Mode Transition
DESCRIPTION: Triggers the current scene transition. This provides the same functionality as the 'Transition' button in studio mode.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_219

LANGUAGE: APIDOC
CODE:
```
TriggerStudioModeTransition:
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
```

----------------------------------------

TITLE: Set Current Program Scene (OBS-WebSocket API)
DESCRIPTION: Sets the current program scene.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_176

LANGUAGE: APIDOC
CODE:
```
SetCurrentProgramScene
  Description: Sets the current program scene.
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    ?sceneName: String - Scene name to set as the current program scene (Value Restrictions: None, Default Behavior: Unknown)
    ?sceneUuid: String - Scene UUID to set as the current program scene (Value Restrictions: None, Default Behavior: Unknown)
```

----------------------------------------

TITLE: Setting Linker Options
DESCRIPTION: Sets specific linker options for the target. On Windows, it adds the `/IGNORE:4099` option, which is used to ignore a specific linker warning.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_11

LANGUAGE: CMake
CODE:
```
target_link_options(obs-websocket PRIVATE $<$<PLATFORM_ID:Windows>:/IGNORE:4099>)
```

----------------------------------------

TITLE: OpenInputPropertiesDialog
DESCRIPTION: Opens the properties dialog of an input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_285

LANGUAGE: APIDOC
CODE:
```
Request Fields:
  inputName (String, optional): Name of the input to open the dialog of.
  inputUuid (String, optional): UUID of the input to open the dialog of.
```

----------------------------------------

TITLE: Linking Required Libraries
DESCRIPTION: Links the necessary libraries to the `obs-websocket` target. This includes linking against OBS core libraries (`OBS::libobs`, `OBS::frontend-api`, `OBS::websocket-api`) and the external dependencies found earlier (Qt6 components, nlohmann_json, Websocket++, Asio, qrcodegencpp). The `PRIVATE` keyword ensures these are only linked for the target itself.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_10

LANGUAGE: CMake
CODE:
```
target_link_libraries(
  obs-websocket
  PRIVATE OBS::libobs
          OBS::frontend-api
          OBS::websocket-api
          Qt::Core
          Qt::Widgets
          Qt::Svg
          Qt::Network
          nlohmann_json::nlohmann_json
          Websocketpp::Websocketpp
          Asio::Asio
          qrcodegencpp::qrcodegencpp)
```

----------------------------------------

TITLE: RequestStatus::ResourceNotFound Error Code
DESCRIPTION: The resource was not found. Resources are any kind of object in obs-websocket, like inputs, profiles, outputs, etc.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_44

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 600
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Add Event Handler Component Source Files
DESCRIPTION: Adds source files for the event handling system, categorizing events by configuration, filters, general, inputs, media inputs, outputs, scene items, scenes, transitions, and UI, along with event subscription types.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_4

LANGUAGE: CMake
CODE:
```
target_sources(
  obs-websocket
  PRIVATE # cmake-format: sortable
          src/eventhandler/EventHandler.cpp
          src/eventhandler/EventHandler.h
          src/eventhandler/EventHandler_Config.cpp
          src/eventhandler/EventHandler_Filters.cpp
          src/eventhandler/EventHandler_General.cpp
          src/eventhandler/EventHandler_Inputs.cpp
          src/eventhandler/EventHandler_MediaInputs.cpp
          src/eventhandler/EventHandler_Outputs.cpp
          src/eventhandler/EventHandler_SceneItems.cpp
          src/eventhandler/EventHandler_Scenes.cpp
          src/eventhandler/EventHandler_Transitions.cpp
          src/eventhandler/EventHandler_Ui.cpp
          src/eventhandler/types/EventSubscription.h)
```

----------------------------------------

TITLE: Identify (OpCode 1)
DESCRIPTION: This message is sent from a freshly connected websocket client to obs-websocket as a response to the `Hello` message. It should contain an authentication string if required, along with PubSub subscriptions and other session parameters. The `rpcVersion` specifies the desired protocol version, and `eventSubscriptions` is a bitmask for subscribing to event categories, with high-volume events requiring explicit subscription.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_7

LANGUAGE: txt
CODE:
```
{
  "rpcVersion": number,
  "authentication": string(optional),
  "eventSubscriptions": number(optional) = (EventSubscription::All)
}
```

LANGUAGE: json
CODE:
```
{
  "op": 1,
  "d": {
    "rpcVersion": 1,
    "authentication": "Dj6cLS+jrNA0HpCArRg0Z/Fc+YHdt2FQfAvgD1mip6Y=",
    "eventSubscriptions": 33
  }
}
```

----------------------------------------

TITLE: RequestStatus::OutputNotRunning Error Code
DESCRIPTION: An output is not running and should be.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_38

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 501
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Define obs-websocket Request Documentation Format
DESCRIPTION: Specifies the JSDoc-like comment structure for documenting requests in obs-websocket, including tags for request parameters (with optional flags, value restrictions, and default behavior), response fields, request type, complexity, RPC version, initial version, and category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/README.md#_snippet_4

LANGUAGE: JavaScript
CODE:
```
/**
 * [description]
 *
 * @requestField [optional flag][field name] | [value type] | [field description] | [value restrictions (only include if the value type is `Number`)] | [default behavior (only include if optional flag is set)]
 * [... more @requestField entries ...]
 *
 * @responseField [field name] | [value type] | [field description]
 * [... more @responseField entries ...]
 *
 * @requestType [type]
 * @complexity [complexity rating, 1-5]
 * @rpcVersion [latest available RPC version, use `-1` unless deprecated.]
 * @initialVersion [first obs-websocket version this is found in]
 * @category [request category]
 * @api requests
 */
```

----------------------------------------

TITLE: Setting AUTORCC Options for Windows
DESCRIPTION: Conditionally appends a specific option (`--format-version 1`) to the `AUTORCC_OPTIONS` property for the target, but only when building on the Windows platform. This option affects how Qt Resource files (`.qrc`) are handled by the resource compiler.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_13

LANGUAGE: CMake
CODE:
```
if(OS_WINDOWS)
  set_property(
    TARGET obs-websocket
    APPEND
    PROPERTY AUTORCC_OPTIONS --format-version 1)
endif()
```

----------------------------------------

TITLE: Set Input Audio Tracks API Documentation
DESCRIPTION: Sets the enable state of audio tracks for a specified input. This API endpoint is part of OBS-websocket, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_205

LANGUAGE: APIDOC
CODE:
```
SetInputAudioTracks:
  Description: Sets the enable state of audio tracks of an input.
  Details:
    Complexity Rating: 2/5
    Latest Supported RPC Version: 1
    Added in: v5.0.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputAudioTracks:
      Type: Object
      Description: Track settings to apply
      Value Restrictions: None
      Default Behavior: N/A
      Optional: false
```

----------------------------------------

TITLE: ObsMediaInputAction::OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PLAY
DESCRIPTION: Play the media input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_74

LANGUAGE: APIDOC
CODE:
```
Identifier Value: OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PLAY
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Event (OpCode 5)
DESCRIPTION: An event coming from OBS has occured. Eg scene switched, source muted.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_11

LANGUAGE: APIDOC
CODE:
```
Sent from: obs-websocket
Sent to: All subscribed and identified clients

Data Keys:
{
  "eventType": string,
  "eventIntent": number,
  "eventData": object(optional)
}
  eventIntent: The original intent required to be subscribed to in order to receive the event.

Example Message:
{
  "op": 5,
  "d": {
    "eventType": "StudioModeStateChanged",
    "eventIntent": 1,
    "eventData": {
      "studioModeEnabled": true
    }
  }
}
```

----------------------------------------

TITLE: ObsMediaInputAction::OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART
DESCRIPTION: Restart the media input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_77

LANGUAGE: APIDOC
CODE:
```
Identifier Value: OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: SceneItemCreated Event
DESCRIPTION: A scene item has been created. This event has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_119

LANGUAGE: APIDOC
CODE:
```
Event: SceneItemCreated
Description: A scene item has been created.
Parameters:
  sceneName (String): Name of the scene the item was added to
  sceneUuid (String): UUID of the scene the item was added to
  sourceName (String): Name of the underlying source (input/scene)
  sourceUuid (String): UUID of the underlying source (input/scene)
  sceneItemId (Number): Numeric ID of the scene item
  sceneItemIndex (Number): Index position of the item
```

----------------------------------------

TITLE: Configure OBS-Websocket Target in CMake
DESCRIPTION: This CMake configuration block sets up the 'obs-websocket' target. It defines compiler warning suppressions for C++ on AppleClang/Clang, links essential OBS, Qt, and third-party libraries like nlohmann_json, Websocketpp, Asio, and qrcodegencpp. It also applies Windows-specific link options and sets general target properties such as folder, prefix, and automatic MOC/UIC/RCC processing.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/CMakeLists.txt#_snippet_9

LANGUAGE: CMake
CODE:
```
$<$<COMPILE_LANG_AND_ID:CXX,AppleClang,Clang>:-Wno-error=deprecated-declarations>
          $<$<COMPILE_LANG_AND_ID:CXX,AppleClang,Clang>:-Wno-error=implicit-int-conversion>
          $<$<COMPILE_LANG_AND_ID:CXX,AppleClang,Clang>:-Wno-error=shorten-64-to-32>
          $<$<COMPILE_LANG_AND_ID:CXX,AppleClang,Clang>:-Wno-comma>
          $<$<COMPILE_LANG_AND_ID:CXX,AppleClang,Clang>:-Wno-quoted-include-in-framework-header>)

target_link_libraries(
  obs-websocket
  PRIVATE OBS::libobs
          OBS::frontend-api
          OBS::websocket-api
          Qt::Core
          Qt::Widgets
          Qt::Svg
          Qt::Network
          nlohmann_json::nlohmann_json
          Websocketpp::Websocketpp
          Asio::Asio
          qrcodegencpp::qrcodegencpp)

target_link_options(obs-websocket PRIVATE $<$<PLATFORM_ID:Windows>:/IGNORE:4099>)

set_target_properties_obs(
  obs-websocket
  PROPERTIES FOLDER plugins
             PREFIX ""
             AUTOMOC ON
             AUTOUIC ON
             AUTORCC ON)

if(OS_WINDOWS)
  set_property(
    TARGET obs-websocket
    APPEND
    PROPERTY AUTORCC_OPTIONS --format-version 1)
endif()
```

----------------------------------------

TITLE: WebSocketOpCode Definitions
DESCRIPTION: Details the various operation codes used in the OBS-Websocket protocol for client-server communication, including identification, events, and requests.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_24

LANGUAGE: APIDOC
CODE:
```
WebSocketOpCode::Hello
  Description: The initial message sent by obs-websocket to newly connected clients.
  Identifier Value: 0
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketOpCode::Identify
  Description: The message sent by a newly connected client to obs-websocket in response to a Hello.
  Identifier Value: 1
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketOpCode::Identified
  Description: The response sent by obs-websocket to a client after it has successfully identified with obs-websocket.
  Identifier Value: 2
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketOpCode::Reidentify
  Description: The message sent by an already-identified client to update identification parameters.
  Identifier Value: 3
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketOpCode::Event
  Description: The message sent by obs-websocket containing an event payload.
  Identifier Value: 5
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketOpCode::Request
  Description: The message sent by a client to obs-websocket to perform a request.
  Identifier Value: 6
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketOpCode::RequestResponse
  Description: The message sent by obs-websocket in response to a particular request from a client.
  Identifier Value: 7
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketOpCode::RequestBatch
  Description: The message sent by a client to obs-websocket to perform a batch of requests.
  Identifier Value: 8
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketOpCode::RequestBatchResponse
  Description: The message sent by obs-websocket in response to a particular batch of requests from a client.
  Identifier Value: 9
  Latest Supported RPC Version: 1
  Added in: v5.0.0
```

----------------------------------------

TITLE: Create Record Chapter API
DESCRIPTION: Adds a new chapter marker to the file currently being recorded. This feature is supported only by Hybrid MP4 as of OBS 30.2.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_278

LANGUAGE: APIDOC
CODE:
```
Method: CreateRecordChapter
Description: Adds a new chapter marker to the file currently being recorded.
Note: As of OBS 30.2.0, the only file format supporting this feature is Hybrid MP4.
Details:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.5.0
Request Fields:
  ?chapterName (String): Name of the new chapter (Value Restrictions: None, Default Behavior: Unknown)
```

----------------------------------------

TITLE: ObsMediaInputAction::OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NONE
DESCRIPTION: No action.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_73

LANGUAGE: APIDOC
CODE:
```
Identifier Value: OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NONE
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: SetStudioModeEnabled
DESCRIPTION: Enables or disables studio mode

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_284

LANGUAGE: APIDOC
CODE:
```
Request Fields:
  studioModeEnabled (Boolean): True == Enabled, False == Disabled.
```

----------------------------------------

TITLE: EventSubscription::Transitions
DESCRIPTION: Subscription value to receive events in the `Transitions` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_61

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 4)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: OBS-websocket General Requests API
DESCRIPTION: API methods for general OBS operations, including retrieving version information, statistics, broadcasting custom events, calling vendor-specific requests, managing hotkeys, and pausing execution.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_137

LANGUAGE: APIDOC
CODE:
```
General Requests:
  GetVersion()
  GetStats()
  BroadcastCustomEvent()
  CallVendorRequest()
  GetHotkeyList()
  TriggerHotkeyByName()
  TriggerHotkeyByKeySequence()
  Sleep()
```

----------------------------------------

TITLE: RequestResponse (OpCode 7)
DESCRIPTION: obs-websocket is responding to a request coming from a client.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_13

LANGUAGE: APIDOC
CODE:
```
Sent from: obs-websocket
Sent to: Identified client which made the request

Data Keys:
{
  "requestType": string,
  "requestId": string,
  "requestStatus": object,
  "responseData": object(optional)
}
  requestType: The `requestType` and `requestId` are simply mirrors of what was sent by the client.
  requestId: The `requestType` and `requestId` are simply mirrors of what was sent by the client.

requestStatus object:
{
  "result": bool,
  "code": number,
  "comment": string(optional)
}
  result: `true` if the request resulted in `RequestStatus::Success`. False if otherwise.
  code: A `RequestStatus` code.
  comment: May be provided by the server on errors to offer further details on why a request failed.

Example Messages:
Successful Response
{
  "op": 7,
  "d": {
    "requestType": "SetCurrentProgramScene",
    "requestId": "f819dcf0-89cc-11eb-8f0e-382c4ac93b9c",
    "requestStatus": {
      "result": true,
      "code": 100
    }
  }
}

Failure Response
{
  "op": 7,
  "d": {
    "requestType": "SetCurrentProgramScene",
    "requestId": "f819dcf0-89cc-11eb-8f0e-382c4ac93b9c",
    "requestStatus": {
      "result": false,
      "code": 608,
      "comment": "Parameter: sceneName"
    }
  }
}
```

----------------------------------------

TITLE: CreateSceneCollection API Method
DESCRIPTION: Creates a new scene collection and immediately switches to it. This is a blocking operation that waits for the collection change to finish.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_157

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  - sceneCollectionName: String - Name for the new scene collection
```

----------------------------------------

TITLE: EventSubscription::Config
DESCRIPTION: Subscription value to receive events in the `Config` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_58

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 1)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: EventSubscription::All
DESCRIPTION: Helper to receive all non-high-volume events.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_68

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (General | Config | Scenes | Inputs | Transitions | Filters | Outputs | SceneItems | MediaInputs | Vendors | Ui)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: RequestStatus::OutputRunning Error Code
DESCRIPTION: An output is running and cannot be in order to perform the request.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_37

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 500
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: OBS WebSocket Request Batch Execution Types
DESCRIPTION: Describes the different execution types for request batches in the OBS WebSocket protocol, influencing how multiple requests are processed.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_27

LANGUAGE: APIDOC
CODE:
```
RequestBatchExecutionType::None
  Description: Not a request batch.
  Identifier Value: -1
  Latest Supported RPC Version: 1
  Added in: v5.0.0

RequestBatchExecutionType::SerialRealtime
  Description: A request batch which processes all requests serially, as fast as possible. Note: To introduce artificial delay, use the `Sleep` request and the `sleepMillis` request field.
  Identifier Value: 0
  Latest Supported RPC Version: 1
  Added in: v5.0.0

RequestBatchExecutionType::SerialFrame
  Description: A request batch type which processes all requests serially, in sync with the graphics thread. Designed to provide high accuracy for animations. Note: To introduce artificial delay, use the `Sleep` request and the `sleepFrames` request field.
  Identifier Value: 1
  Latest Supported RPC Version: 1
  Added in: v5.0.0

RequestBatchExecutionType::Parallel
  Description: A request batch type which processes all requests using all available threads in the thread pool. Note: This is mainly experimental, and only really shows its colors during requests which require lots of active processing, like `GetSourceScreenshot`.
  Identifier Value: 2
  Latest Supported RPC Version: 1
  Added in: v5.0.0
```

----------------------------------------

TITLE: SetInputVolume API Method
DESCRIPTION: Sets the volume setting of an input. This method allows specifying volume either in multiplication factor (mul) or decibels (dB).

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_197

LANGUAGE: APIDOC
CODE:
```
SetInputVolume:
  Description: Sets the volume setting of an input.
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - Name: inputName (Optional)
      Type: String
      Description: Name of the input to set the volume of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputUuid (Optional)
      Type: String
      Description: UUID of the input to set the volume of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputVolumeMul (Optional)
      Type: Number
      Description: Volume setting in mul
      Value Restrictions: ">= 0, <= 20"
      Default Behavior: inputVolumeDb should be specified
    - Name: inputVolumeDb (Optional)
      Type: Number
      Description: Volume setting in dB
      Value Restrictions: ">= -100, <= 26"
      Default Behavior: inputVolumeMul should be specified
```

----------------------------------------

TITLE: API Event: InputCreated (OBS-websocket)
DESCRIPTION: Documents the 'InputCreated' event, which is triggered when a new input is successfully created in OBS. It provides comprehensive details about the newly created input, including its name, UUID, kind, settings, and default settings.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_95

LANGUAGE: APIDOC
CODE:
```
Event: InputCreated
Description: An input has been created.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
- inputKind: String (The kind of the input)
- unversionedInputKind: String (The unversioned kind of input (aka no _v2 stuff))
- inputKindCaps: Number (Bitflag value for the caps that an input supports. See obs_source_info.output_flags in the libobs docs)
- inputSettings: Object (The settings configured to the input when it was created)
- defaultInputSettings: Object (The default settings for the input)
```

----------------------------------------

TITLE: Set Source Filter Settings API
DESCRIPTION: Applies new settings to a specific source filter. The 'overlay' parameter determines if settings are merged with existing ones or if defaults are reset first. The source can be identified by name or UUID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_229

LANGUAGE: APIDOC
CODE:
```
SetSourceFilterSettings:
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    ?sourceName: String - Name of the source the filter is on
    ?sourceUuid: String - UUID of the source the filter is on
    filterName: String - Name of the filter to set the settings of
    filterSettings: Object - Object of settings to apply
    ?overlay: Boolean - True == apply the settings on top of existing ones, False == reset the input to its defaults, then apply settings. (default: true)
```

----------------------------------------

TITLE: Create Source Filter
DESCRIPTION: Creates a new filter and adds it to the specified source.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_224

LANGUAGE: APIDOC
CODE:
```
CreateSourceFilter:
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    sourceName: String - Name of the source to add the filter to (Optional).
    sourceUuid: String - UUID of the source to add the filter to (Optional).
    filterName: String - Name of the new filter to be created.
    filterKind: String - The kind of filter to be created.
    filterSettings: Object - Settings object to initialize the filter with (Optional, Default: Default settings used).
```

----------------------------------------

TITLE: Defining RequestBatchResponse Message Data Keys (OpCode 9) - obs-websocket
DESCRIPTION: This text snippet outlines the data keys for the 'RequestBatchResponse' message sent by obs-websocket in response to a batch request. It includes the 'requestId' mirroring the batch request and an array of 'results' for each request in the batch.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_19

LANGUAGE: txt
CODE:
```
{
  "requestId": string,
  "results": array<object>
}
```

----------------------------------------

TITLE: TriggerHotkeyByKeySequence API
DESCRIPTION: Triggers a hotkey using a sequence of keys. Note: Hotkey functionality in obs-websocket comes as-is, and we do not guarantee support if things are broken. In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_151

LANGUAGE: APIDOC
CODE:
```
TriggerHotkeyByKeySequence:
  Description: Triggers a hotkey using a sequence of keys. Note: Hotkey functionality in obs-websocket comes as-is, and we do not guarantee support if things are broken. In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests.
  Complexity Rating: 4/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    keyId:
      Type: String
      Description: The OBS key ID to use. See https://github.com/obsproject/obs-studio/blob/master/libobs/obs-hotkeys.h
      Value Restrictions: None
      Default Behavior: Not pressed
    keyModifiers:
      Type: Object
      Description: Object containing key modifiers to apply
      Value Restrictions: None
      Default Behavior: Ignored
      Properties:
        shift:
          Type: Boolean
          Description: Press Shift
          Value Restrictions: None
          Default Behavior: Not pressed
        control:
          Type: Boolean
          Description: Press CTRL
          Value Restrictions: None
          Default Behavior: Not pressed
        alt:
          Type: Boolean
          Description: Press ALT
          Value Restrictions: None
          Default Behavior: Not pressed
        command:
          Type: Boolean
          Description: Press CMD (Mac)
          Value Restrictions: None
          Default Behavior: Not pressed
```

----------------------------------------

TITLE: RequestStatus::NotReady Error Code
DESCRIPTION: The server is not ready to handle the request. This usually occurs during OBS scene collection change or exit. Requests may be tried again after a delay if this code is given.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_29

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 207
Latest Supported RPC Version: 1
Added in v5.3.0
```

----------------------------------------

TITLE: RequestStatus::StudioModeNotActive Error Code
DESCRIPTION: Studio mode is not active and should be.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_43

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 506
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: SetInputAudioBalance API Method
DESCRIPTION: Sets the audio balance of an input. The new audio balance value must be between 0.0 and 1.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_199

LANGUAGE: APIDOC
CODE:
```
SetInputAudioBalance:
  Description: Sets the audio balance of an input.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - Name: inputName (Optional)
      Type: String
      Description: Name of the input to set the audio balance of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputUuid (Optional)
      Type: String
      Description: UUID of the input to set the audio balance of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputAudioBalance
      Type: Number
      Description: New audio balance value
      Value Restrictions: ">= 0.0, <= 1.0"
      Default Behavior: N/A
```

----------------------------------------

TITLE: OBS-websocket Sources Requests API
DESCRIPTION: API methods for interacting with OBS sources, including checking their active status and capturing or saving screenshots of specific sources.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_139

LANGUAGE: APIDOC
CODE:
```
Sources Requests:
  GetSourceActive()
  GetSourceScreenshot()
  SaveSourceScreenshot()
```

----------------------------------------

TITLE: obs-websocket Message Types (OpCodes) Overview
DESCRIPTION: Outlines the various OpCodes used in the obs-websocket protocol to categorize different message types. These codes define the purpose of a message, such as initial handshakes, event notifications, or request/response cycles.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_1

LANGUAGE: APIDOC
CODE:
```
Message Types (OpCodes):
- OpCode 0: Hello
- OpCode 1: Identify
- OpCode 2: Identified
- OpCode 3: Reidentify
- OpCode 5: Event
- OpCode 6: Request
- OpCode 7: RequestResponse
- OpCode 8: RequestBatch
- OpCode 9: RequestBatchResponse
```

----------------------------------------

TITLE: Define obs-websocket Enum Documentation Format
DESCRIPTION: Specifies the JSDoc-like comment structure for documenting enums in obs-websocket, including tags for identifier, value, type, RPC version, initial version, and API category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/README.md#_snippet_0

LANGUAGE: JavaScript
CODE:
```
/**
* [description]
*
* @enumIdentifier [identifier]
* @enumValue [value]
* @enumType [type]
* @rpcVersion [latest available RPC version, use `-1` unless deprecated.]
* @initialVersion [first obs-websocket version this is found in]
* @api enums
*/
```

----------------------------------------

TITLE: SaveSourceScreenshot API Method
DESCRIPTION: Saves a screenshot of a source to the filesystem. The `imageWidth` and `imageHeight` parameters are treated as "scale to inner", meaning the smallest ratio will be used and the aspect ratio of the original resolution is kept. If `imageWidth` and `imageHeight` are not specified, the compressed image will use the full resolution of the source. Compatible with inputs and scenes.

- Complexity Rating: 3/5
- Latest Supported RPC Version: 1
- Added in v5.0.0

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_172

LANGUAGE: APIDOC
CODE:
```
SaveSourceScreenshot:
  Request Fields:
    ?sourceName: String (Name of the source to take a screenshot of)
      Value Restrictions: None
      Default Behavior: Unknown
    ?sourceUuid: String (UUID of the source to take a screenshot of)
      Value Restrictions: None
      Default Behavior: Unknown
    imageFormat: String (Image compression format to use. Use `GetVersion` to get compatible image formats)
      Value Restrictions: None
      Default Behavior: N/A
    imageFilePath: String (Path to save the screenshot file to. Eg. `C:\Users\user\Desktop\screenshot.png`)
      Value Restrictions: None
      Default Behavior: N/A
    ?imageWidth: Number (Width to scale the screenshot to)
      Value Restrictions: >= 8, <= 4096
      Default Behavior: Source value is used
    ?imageHeight: Number (Height to scale the screenshot to)
      Value Restrictions: >= 8, <= 4096
      Default Behavior: Source value is used
    ?imageCompressionQuality: Number (Compression quality to use. 0 for high compression, 100 for uncompressed. -1 to use "default" (whatever that means, idk))
      Value Restrictions: >= -1, <= 100
      Default Behavior: -1
```

----------------------------------------

TITLE: Identified (OpCode 2)
DESCRIPTION: The identify request was received and validated, and the connection is now ready for normal operation.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_9

LANGUAGE: APIDOC
CODE:
```
Sent from: obs-websocket
Sent to: Freshly identified client

Data Keys:
{
  "negotiatedRpcVersion": number
}
  negotiatedRpcVersion: If rpc version negotiation succeeds, the server determines the RPC version to be used and gives it to the client as `negotiatedRpcVersion`.

Example Message:
{
  "op": 2,
  "d": {
    "negotiatedRpcVersion": 1
  }
}
```

----------------------------------------

TITLE: EventSubscription::Vendors
DESCRIPTION: Subscription value to receive the `VendorEvent` event.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_66

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 9)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: API Event: InputSettingsChanged (OBS-websocket)
DESCRIPTION: Documents the 'InputSettingsChanged' event, fired when an input's settings are updated. This event provides the input's name, UUID, and the new settings object. Note that canceling changes in the properties dialog may also trigger this event.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_98

LANGUAGE: APIDOC
CODE:
```
Event: InputSettingsChanged
Description: An input's settings have changed (been updated).
Note: On some inputs, changing values in the properties dialog will cause an immediate update. Pressing the "Cancel" button will revert the settings, resulting in another event being fired.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in v5.4.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
- inputSettings: Object (New settings object of the input)
```

----------------------------------------

TITLE: RequestStatus::StudioModeActive Error Code
DESCRIPTION: Studio mode is active and cannot be.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_42

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 505
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Set Scene Transition Override API Documentation
DESCRIPTION: Sets the scene transition overridden for a specific scene. This method allows specifying a custom transition name and duration, or removing an existing override by setting values to `null`.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_183

LANGUAGE: APIDOC
CODE:
```
SetSceneSceneTransitionOverride:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - sceneName (String): Name of the scene. Value Restrictions: None. Default Behavior: Unknown.
    - sceneUuid (String): UUID of the scene. Value Restrictions: None. Default Behavior: Unknown.
    - transitionName (String): Name of the scene transition to use as override. Specify `null` to remove. Value Restrictions: None. Default Behavior: Unchanged.
    - transitionDuration (Number): Duration to use for any overridden transition. Specify `null` to remove. Value Restrictions: >= 50, <= 20000. Default Behavior: Unchanged.
```

----------------------------------------

TITLE: OBS-Websocket API: ObsMediaInputAction Enum
DESCRIPTION: Defines actions that can be performed on media inputs, such as navigating playlist items. These actions are used to control media playback within OBS.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_78

LANGUAGE: APIDOC
CODE:
```
ObsMediaInputAction:
  OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NEXT:
    Description: Go to the next playlist item.
    Identifier Value: OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NEXT
    Latest Supported RPC Version: 1
    Added in: v5.0.0
  OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PREVIOUS:
    Description: Go to the previous playlist item.
    Identifier Value: OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PREVIOUS
    Latest Supported RPC Version: 1
    Added in: v5.0.0
```

----------------------------------------

TITLE: EventSubscription::Ui
DESCRIPTION: Subscription value to receive events in the `Ui` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_67

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 10)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: SetInputAudioSyncOffset API Method
DESCRIPTION: Sets the audio sync offset of an input. The offset is specified in milliseconds and has a defined range.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_201

LANGUAGE: APIDOC
CODE:
```
SetInputAudioSyncOffset:
  Description: Sets the audio sync offset of an input.
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - Name: inputName (Optional)
      Type: String
      Description: Name of the input to set the audio sync offset of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputUuid (Optional)
      Type: String
      Description: UUID of the input to set the audio sync offset of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputAudioSyncOffset
      Type: Number
      Description: New audio sync offset in milliseconds
      Value Restrictions: ">= -950, <= 20000"
      Default Behavior: N/A
```

----------------------------------------

TITLE: Defining RequestBatch Message Data Keys (OpCode 8) - obs-websocket
DESCRIPTION: This text snippet defines the data keys for the 'RequestBatch' message, used by clients to send multiple requests serially. It includes 'requestId', optional 'haltOnFailure', optional 'executionType', and an array of 'requests'.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_18

LANGUAGE: txt
CODE:
```
{
  "requestId": string,
  "haltOnFailure": bool(optional) = false,
  "executionType": number(optional) = RequestBatchExecutionType::SerialRealtime
  "requests": array<object>
}
```

----------------------------------------

TITLE: EventSubscription::SceneItems
DESCRIPTION: Subscription value to receive events in the `SceneItems` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_64

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 7)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: EventSubscription::General
DESCRIPTION: Subscription value to receive events in the `General` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_57

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 0)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: OBS-WebSocket Base Message Structure (OpCode and Data)
DESCRIPTION: Defines the fundamental JSON structure for all low-level messages exchanged with obs-websocket, comprising an operation code ('op') and a data payload ('d').

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_3

LANGUAGE: txt
CODE:
```
{
  "op": number,
  "d": object
}
```

----------------------------------------

TITLE: SetCurrentSceneTransition
DESCRIPTION: Sets the current scene transition. Small note: While the namespace of scene transitions is generally unique, that uniqueness is not a guarantee as it is with other resources like inputs.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_215

LANGUAGE: APIDOC
CODE:
```
SetCurrentSceneTransition:
  Description: Sets the current scene transition. Small note: While the namespace of scene transitions is generally unique, that uniqueness is not a guarantee as it is with other resources like inputs.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - transitionName (String): Name of the transition to make active [Value Restrictions: None] [Default Behavior: N/A]
```

----------------------------------------

TITLE: Enumeration Declarations (Enums)
DESCRIPTION: General section indicating the presence of enumeration declarations referenced throughout the obs-websocket protocol.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_15

LANGUAGE: APIDOC
CODE:
```
Enums:
  Description: These are enumeration declarations, which are referenced throughout obs-websocket's protocol.
```

----------------------------------------

TITLE: SceneItemEnableStateChanged Event
DESCRIPTION: A scene item's enable state has changed. This event has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_122

LANGUAGE: APIDOC
CODE:
```
Event: SceneItemEnableStateChanged
Description: A scene item's enable state has changed.
Parameters:
  sceneName (String): Name of the scene the item is in
  sceneUuid (String): UUID of the scene the item is in
  sceneItemId (Number): Numeric ID of the scene item
  sceneItemEnabled (Boolean): Whether the scene item is enabled (visible)
```

----------------------------------------

TITLE: SourceFilterSettingsChanged Event
DESCRIPTION: An source filter's settings have changed (been updated). This event has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.4.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_117

LANGUAGE: APIDOC
CODE:
```
Event: SourceFilterSettingsChanged
Description: An source filter's settings have changed (been updated).
Parameters:
  sourceName (String): Name of the source the filter is on
  filterName (String): Name of the filter
  filterSettings (Object): New settings object of the filter
```

----------------------------------------

TITLE: OBS-WebSocket Connection Rules and Error Handling
DESCRIPTION: Details various conditions under which an obs-websocket connection may be closed, including subprotocol mismatches, unrecognized messages, and incorrect client identification sequences.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_1

LANGUAGE: APIDOC
CODE:
```
Connection Notes:
- If a binary frame is received when using the obswebsocket.json (default) subprotocol, or a text frame is received while using the obswebsocket.msgpack subprotocol, the connection is closed with WebSocketCloseCode::MessageDecodeError.
- The obs-websocket server listens for any messages containing a request-type field in the first level JSON from unidentified clients. If a message matches, the connection is closed with WebSocketCloseCode::UnsupportedRpcVersion and a warning is logged.
- If a message with a messageType is not recognized to the obs-websocket server, the connection is closed with WebSocketCloseCode::UnknownOpCode.
- At no point may the client send any message other than a single Identify before it has received an Identified. Doing so will result in the connection being closed with WebSocketCloseCode::NotIdentified.
```

----------------------------------------

TITLE: EventSubscription::Outputs
DESCRIPTION: Subscription value to receive events in the `Outputs` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_63

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 6)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: GetSceneItemIndex API Method
DESCRIPTION: Retrieves the index position of a scene item within its scene. An index of 0 corresponds to the bottom of the source list in the OBS UI, indicating its z-order.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_244

LANGUAGE: APIDOC
CODE:
```
Method: GetSceneItemIndex
Description: Gets the index position of a scene item in a scene. An index of 0 is at the bottom of the source list in the UI. Scenes and Groups.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in: v5.0.0
Request Fields:
  - Name: ?sceneName, Type: String, Description: Name of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: ?sceneUuid, Type: String, Description: UUID of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: sceneItemId, Type: Number, Description: Numeric ID of the scene item, Value Restrictions: >= 0, Default Behavior: N/A
Response Fields:
  - Name: sceneItemIndex, Type: Number, Description: Index position of the scene item
```

----------------------------------------

TITLE: SetRecordDirectory
DESCRIPTION: Sets the current directory that the record output writes files to.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_169

LANGUAGE: APIDOC
CODE:
```
Method: SetRecordDirectory
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.3.0

Request Fields:
  recordDirectory: String - Output directory
```

----------------------------------------

TITLE: EventSubscription::Inputs
DESCRIPTION: Subscription value to receive events in the `Inputs` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_60

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 3)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: CallVendorRequest API
DESCRIPTION: Call a request registered to a vendor. A vendor is a unique name registered by a third-party plugin or script, which allows for custom requests and events to be added to obs-websocket. If a plugin or script implements vendor requests or events, documentation is expected to be provided with them.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_148

LANGUAGE: APIDOC
CODE:
```
CallVendorRequest:
  Description: Call a request registered to a vendor. A vendor is a unique name registered by a third-party plugin or script, which allows for custom requests and events to be added to obs-websocket. If a plugin or script implements vendor requests or events, documentation is expected to be provided with them.
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    vendorName:
      Type: String
      Description: Name of the vendor to use
      Value Restrictions: None
      Default Behavior: N/A
    requestType:
      Type: String
      Description: The request type to call
      Value Restrictions: None
      Default Behavior: N/A
    requestData:
      Type: Object
      Description: Object containing appropriate request data
      Value Restrictions: None
      Default Behavior: {}
  Response Fields:
    vendorName:
      Type: String
      Description: Echoed of vendorName
    requestType:
      Type: String
      Description: Echoed of requestType
    responseData:
      Type: Object
      Description: Object containing appropriate response data. {} if request does not provide any response data
```

----------------------------------------

TITLE: OpenInputInteractDialog
DESCRIPTION: Opens the interact dialog of an input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_287

LANGUAGE: APIDOC
CODE:
```
Request Fields:
  inputName (String, optional): Name of the input to open the dialog of.
  inputUuid (String, optional): UUID of the input to open the dialog of.
```

----------------------------------------

TITLE: Set Media Input Cursor API
DESCRIPTION: Sets the playback cursor position for a specified media input. This request does not perform bounds checking.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_280

LANGUAGE: APIDOC
CODE:
```
Method: SetMediaInputCursor
Description: Sets the cursor position of a media input.
This request does not perform bounds checking of the cursor position.
Details:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
Request Fields:
  ?inputName (String): Name of the media input (Value Restrictions: None, Default Behavior: Unknown)
  ?inputUuid (String): UUID of the media input (Value Restrictions: None, Default Behavior: Unknown)
  mediaCursor (Number): New cursor position to set (Value Restrictions: >= 0, Default Behavior: N/A)
```

----------------------------------------

TITLE: OpenInputFiltersDialog
DESCRIPTION: Opens the filters dialog of an input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_286

LANGUAGE: APIDOC
CODE:
```
Request Fields:
  inputName (String, optional): Name of the input to open the dialog of.
  inputUuid (String, optional): UUID of the input to open the dialog of.
```

----------------------------------------

TITLE: OBS-WebSocket: SceneCreated Event
DESCRIPTION: This event is fired when a new scene is created within OBS. It provides details about the new scene, including its name, UUID, and whether it's a group.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_89

LANGUAGE: APIDOC
CODE:
```
Event: SceneCreated
Description: A new scene has been created.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  sceneName: String - Name of the new scene
  sceneUuid: String - UUID of the new scene
  isGroup: Boolean - Whether the new scene is a group
```

----------------------------------------

TITLE: EventSubscription::MediaInputs
DESCRIPTION: Subscription value to receive events in the `MediaInputs` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_65

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 8)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: ObsMediaInputAction Enumeration
DESCRIPTION: Defines actions that can be performed on media inputs in OBS-Websocket, such as play, pause, or stop.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_22

LANGUAGE: APIDOC
CODE:
```
ObsMediaInputAction:
  OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NONE
  OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PLAY
  OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PAUSE
  OBS_WEBSOCKET_MEDIA_INPUT_ACTION_STOP
  OBS_WEBSOCKET_MEDIA_INPUT_ACTION_RESTART
  OBS_WEBSOCKET_MEDIA_INPUT_ACTION_NEXT
  OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PREVIOUS
```

----------------------------------------

TITLE: EventSubscription::Scenes
DESCRIPTION: Subscription value to receive events in the `Scenes` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_59

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 2)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: OBS-WebSocket Base Message Structure
DESCRIPTION: Defines the fundamental structure for all messages sent to and from obs-websocket, including the operation code ('op') and data payload ('d').

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_4

LANGUAGE: txt
CODE:
```
{
  "op": number,
  "d": object
}
```

----------------------------------------

TITLE: RequestStatus::ResourceActionFailed Error Code
DESCRIPTION: Performing an action on the resource failed.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_53

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 701
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Set Scene Name (OBS-WebSocket API)
DESCRIPTION: Sets the name of a scene (rename).

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_181

LANGUAGE: APIDOC
CODE:
```
SetSceneName
  Description: Sets the name of a scene (rename).
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    ?sceneName: String - Name of the scene to be renamed (Value Restrictions: None, Default Behavior: Unknown)
    ?sceneUuid: String - UUID of the scene to be renamed (Value Restrictions: None, Default Behavior: Unknown)
    newSceneName: String - New name for the scene (Value Restrictions: None, Default Behavior: N/A)
```

----------------------------------------

TITLE: Save Replay Buffer Content (OBS-Websocket API)
DESCRIPTION: Saves the current contents of the replay buffer to a file. This action typically creates a video file from the buffered footage.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_256

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: TriggerMediaInputAction
DESCRIPTION: Triggers an action on a media input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_282

LANGUAGE: APIDOC
CODE:
```
Request Fields:
  inputName (String, optional): Name of the media input. Default: Unknown.
  inputUuid (String, optional): UUID of the media input. Default: Unknown.
  mediaAction (String): Identifier of the `ObsMediaInputAction` enum.
```

----------------------------------------

TITLE: GetSceneItemId API Reference
DESCRIPTION: Searches a scene for a source, and returns its ID. This method can be used with either scene name or UUID, and allows for skipping matches.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_233

LANGUAGE: APIDOC
CODE:
```
GetSceneItemId:
  Request Fields:
    ?sceneName: String - Name of the scene or group to search in
    ?sceneUuid: String - UUID of the scene or group to search in
    sourceName: String - Name of the source to find
    ?searchOffset: Number - Number of matches to skip during search. >= 0 means first forward. -1 means last (top) item
  Response Fields:
    sceneItemId: Number - Numeric ID of the scene item
```

----------------------------------------

TITLE: Set Input Name API Documentation
DESCRIPTION: Renames an existing input in OBS. This allows updating the display name of a source using either its current name or UUID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_189

LANGUAGE: APIDOC
CODE:
```
SetInputName:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - inputName (String): Current input name. Value Restrictions: None. Default Behavior: Unknown.
    - inputUuid (String): Current input UUID. Value Restrictions: None. Default Behavior: Unknown.
    - newInputName (String): New name for the input. Value Restrictions: None. Default Behavior: N/A.
```

----------------------------------------

TITLE: SourceFilterCreated Event
DESCRIPTION: Documents the 'SourceFilterCreated' event, triggered when a new filter is added to a source. It includes comprehensive details about the new filter, such as its name, kind, index, and both configured and default settings.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_114

LANGUAGE: APIDOC
CODE:
```
Event: SourceFilterCreated
Description: A filter has been added to a source.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  sourceName: String - Name of the source the filter was added to
  filterName: String - Name of the filter
  filterKind: String - The kind of the filter
  filterIndex: Number - Index position of the filter
  filterSettings: Object - The settings configured to the filter when it was created
  defaultFilterSettings: Object - The default settings for the filter
```

----------------------------------------

TITLE: EventSubscription Enumeration
DESCRIPTION: Defines flags for subscribing to different categories of events within OBS-WebSocket, allowing clients to filter event notifications.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_20

LANGUAGE: APIDOC
CODE:
```
EventSubscription:
  None
  General
  Config
  Scenes
  Inputs
```

----------------------------------------

TITLE: Identified (OpCode 2)
DESCRIPTION: This message is sent from obs-websocket to a freshly identified client. It indicates that the identify request was received and validated, and the connection is now ready for normal operation. If RPC version negotiation succeeds, the server determines the RPC version to be used and provides it to the client as `negotiatedRpcVersion`.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_8

LANGUAGE: txt
CODE:
```
{
  "negotiatedRpcVersion": number
}
```

LANGUAGE: json
CODE:
```
{
  "op": 2,
  "d": {
    "negotiatedRpcVersion": 1
  }
}
```

----------------------------------------

TITLE: SceneItemSelected Event
DESCRIPTION: A scene item has been selected in the Ui. This event has a complexity rating of 2/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_124

LANGUAGE: APIDOC
CODE:
```
Event: SceneItemSelected
Description: A scene item has been selected in the Ui.
Parameters:
  sceneName (String): Name of the scene the item is in
  sceneUuid (String): UUID of the scene the item is in
  sceneItemId (Number): Numeric ID of the scene item
```

----------------------------------------

TITLE: TriggerHotkeyByName API
DESCRIPTION: Triggers a hotkey using its name. See GetHotkeyList. Note: Hotkey functionality in obs-websocket comes as-is, and we do not guarantee support if things are broken. In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_150

LANGUAGE: APIDOC
CODE:
```
TriggerHotkeyByName:
  Description: Triggers a hotkey using its name. See GetHotkeyList. Note: Hotkey functionality in obs-websocket comes as-is, and we do not guarantee support if things are broken. In 9/10 usages of hotkey requests, there exists a better, more reliable method via other requests.
  Complexity Rating: 4/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    hotkeyName:
      Type: String
      Description: Name of the hotkey to trigger
      Value Restrictions: None
      Default Behavior: N/A
    contextName:
      Type: String
      Description: Name of context of the hotkey to trigger
      Value Restrictions: None
      Default Behavior: Unknown
```

----------------------------------------

TITLE: Document OBS-websocket VendorEvent
DESCRIPTION: Documents the `VendorEvent`, an event emitted by a third-party plugin or script registered as a vendor. It allows for custom requests and events within obs-websocket and includes vendor-specific data.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_81

LANGUAGE: APIDOC
CODE:
```
VendorEvent:
  Description: An event has been emitted from a vendor.
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Data Fields:
    vendorName: String - Name of the vendor emitting the event
    eventType: String - Vendor-provided event typedef
    eventData: Object - Vendor-provided event data. {} if event does not provide any data
```

----------------------------------------

TITLE: SetCurrentProfile API Method
DESCRIPTION: Switches to a specified profile. This method allows changing the active OBS profile.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_159

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  - profileName: String - Name of the profile to switch to
```

----------------------------------------

TITLE: SourceFilterEnableStateChanged Event
DESCRIPTION: A source filter's enable state has changed. This event has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_118

LANGUAGE: APIDOC
CODE:
```
Event: SourceFilterEnableStateChanged
Description: A source filter's enable state has changed.
Parameters:
  sourceName (String): Name of the source the filter is on
  filterName (String): Name of the filter
  filterEnabled (Boolean): Whether the filter is enabled
```

----------------------------------------

TITLE: GetSceneItemEnabled API Method
DESCRIPTION: Retrieves the current enable state (visibility) of a specific scene item. This applies to items within both scenes and groups, indicating whether they are currently visible or hidden.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_240

LANGUAGE: APIDOC
CODE:
```
Method: GetSceneItemEnabled
Description: Gets the enable state of a scene item. Scenes and Groups.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in: v5.0.0
Request Fields:
  - Name: ?sceneName, Type: String, Description: Name of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: ?sceneUuid, Type: String, Description: UUID of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: sceneItemId, Type: Number, Description: Numeric ID of the scene item, Value Restrictions: >= 0, Default Behavior: N/A
Response Fields:
  - Name: sceneItemEnabled, Type: Boolean, Description: Whether the scene item is enabled. true for enabled, false for disabled
```

----------------------------------------

TITLE: GetSceneItemTransform API Reference
DESCRIPTION: Retrieves the transform and crop information for a specific scene item, identified by its numeric ID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_238

LANGUAGE: APIDOC
CODE:
```
GetSceneItemTransform:
  Request Fields:
    ?sceneName: String - Name of the scene the item is in
    ?sceneUuid: String - UUID of the scene the item is in
    sceneItemId: Number - Numeric ID of the scene item
  Response Fields:
    sceneItemTransform: Object - Object containing scene item transform info
```

----------------------------------------

TITLE: SetSceneItemEnabled API Method
DESCRIPTION: Sets the enable state (visibility) of a specific scene item. This allows toggling the visibility of items within scenes and groups.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_241

LANGUAGE: APIDOC
CODE:
```
Method: SetSceneItemEnabled
Description: Sets the enable state of a scene item. Scenes and Groups.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in: v5.0.0
Request Fields:
  - Name: ?sceneName, Type: String, Description: Name of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: ?sceneUuid, Type: String, Description: UUID of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: sceneItemId, Type: Number, Description: Numeric ID of the scene item, Value Restrictions: >= 0, Default Behavior: N/A
  - Name: sceneItemEnabled, Type: Boolean, Description: New enable state of the scene item, Value Restrictions: None, Default Behavior: N/A
```

----------------------------------------

TITLE: SetCurrentSceneCollection API Method
DESCRIPTION: Switches to a specified scene collection. This operation is blocking, meaning it will wait until the collection change is complete before returning.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_156

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  - sceneCollectionName: String - Name of the scene collection to switch to
```

----------------------------------------

TITLE: API Event: InputAudioSyncOffsetChanged (OBS-websocket)
DESCRIPTION: Documents the 'InputAudioSyncOffsetChanged' event, which occurs when an input's audio sync offset is adjusted. It provides the input's name, UUID, and the new sync offset value in milliseconds.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_104

LANGUAGE: APIDOC
CODE:
```
Event: InputAudioSyncOffsetChanged
Description: The sync offset of an input has changed.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
- inputAudioSyncOffset: Number (New sync offset in milliseconds)
```

----------------------------------------

TITLE: SetSceneItemIndex API Method
DESCRIPTION: Sets the index position of a scene item within its scene. This allows reordering items in the z-axis, with an index of 0 placing the item at the bottom of the source list.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_245

LANGUAGE: APIDOC
CODE:
```
Method: SetSceneItemIndex
Description: Sets the index position of a scene item in a scene. Scenes and Groups.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in: v5.0.0
Request Fields:
  - Name: ?sceneName, Type: String, Description: Name of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: ?sceneUuid, Type: String, Description: UUID of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: sceneItemId, Type: Number, Description: Numeric ID of the scene item, Value Restrictions: >= 0, Default Behavior: N/A
  - Name: sceneItemIndex, Type: Number, Description: New index position of the scene item, Value Restrictions: >= 0, Default Behavior: N/A
```

----------------------------------------

TITLE: Event (OpCode 5)
DESCRIPTION: This message is sent from obs-websocket to all subscribed and identified clients when an event originating from OBS occurs, such as a scene switch or source mute. The `eventIntent` field indicates the original intent required for a client to have subscribed to in order to receive this specific event.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_10

LANGUAGE: txt
CODE:
```
{
  "eventType": string,
  "eventIntent": number,
  "eventData": object(optional)
}
```

LANGUAGE: json
CODE:
```
{
  "op": 5,
  "d": {
    "eventType": "StudioModeStateChanged",
    "eventIntent": 1,
    "eventData": {
      "studioModeEnabled": true
    }
  }
}
```

----------------------------------------

TITLE: EventSubscription::InputVolumeMeters
DESCRIPTION: Subscription value to receive the `InputVolumeMeters` high-volume event.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_69

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 16)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: RequestStatus::InvalidInputKind Error Code
DESCRIPTION: The specified input (obs_source_t-OBS_SOURCE_TYPE_INPUT) had the wrong kind.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_49

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 605
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: WebSocketCloseCode Definitions
DESCRIPTION: Details the specific close codes used in the OBS-Websocket protocol to indicate reasons for connection termination.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_25

LANGUAGE: APIDOC
CODE:
```
WebSocketCloseCode::DontClose
  Description: For internal use only to tell the request handler not to perform any close action.
  Identifier Value: 0
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::UnknownReason
  Description: Unknown reason, should never be used.
  Identifier Value: 4000
  Latest Supported RPC Version: 1
  Added in: v5.0.0
```

----------------------------------------

TITLE: Resume Record Output API
DESCRIPTION: Resumes a paused recording for the OBS record output.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_276

LANGUAGE: APIDOC
CODE:
```
Method: ResumeRecord
Description: Resumes the record output.
Details:
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
```

----------------------------------------

TITLE: RequestBatchExecutionType Enumeration
DESCRIPTION: Defines the different methods for executing a batch of requests, allowing for serial, real-time, frame-based, or parallel processing.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_18

LANGUAGE: APIDOC
CODE:
```
RequestBatchExecutionType:
  None
  SerialRealtime
  SerialFrame
  Parallel
```

----------------------------------------

TITLE: BroadcastCustomEvent API
DESCRIPTION: Broadcasts a CustomEvent to all WebSocket clients. Receivers are clients which are identified and subscribed.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_147

LANGUAGE: APIDOC
CODE:
```
BroadcastCustomEvent:
  Description: Broadcasts a CustomEvent to all WebSocket clients. Receivers are clients which are identified and subscribed.
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    eventData:
      Type: Object
      Description: Data payload to emit to all receivers
      Value Restrictions: None
      Default Behavior: N/A
```

----------------------------------------

TITLE: DuplicateSceneItem API Reference
DESCRIPTION: Duplicates an existing scene item, preserving its transform and crop information. The duplicated item can be placed in the same or a different scene.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_237

LANGUAGE: APIDOC
CODE:
```
DuplicateSceneItem:
  Request Fields:
    ?sceneName: String - Name of the scene the item is in
    ?sceneUuid: String - UUID of the scene the item is in
    sceneItemId: Number - Numeric ID of the scene item
    ?destinationSceneName: String - Name of the scene to create the duplicated item in
    ?destinationSceneUuid: String - UUID of the scene to create the duplicated item in
  Response Fields:
    sceneItemId: Number - Numeric ID of the duplicated scene item
```

----------------------------------------

TITLE: RequestStatus::CannotAct
DESCRIPTION: The combination of request fields cannot be used to perform an action.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_55

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 703
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Document OBS-websocket ExitStarted Event
DESCRIPTION: Documents the `ExitStarted` event, which is emitted when OBS begins its shutdown process. It is a simple event with no associated data fields.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_80

LANGUAGE: APIDOC
CODE:
```
ExitStarted:
  Description: OBS has begun the shutdown process.
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
```

----------------------------------------

TITLE: EventSubscription Enumeration
DESCRIPTION: Defines various categories for event subscriptions within OBS-Websocket, allowing clients to filter and receive specific types of events.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_21

LANGUAGE: APIDOC
CODE:
```
EventSubscription:
  Transitions
  Filters
  Outputs
  SceneItems
  MediaInputs
  Vendors
  Ui
  All
  InputVolumeMeters
  InputActiveStateChanged
  InputShowStateChanged
  SceneItemTransformChanged
```

----------------------------------------

TITLE: Toggle Record Output API
DESCRIPTION: Toggles the active state of the OBS record output, switching between recording and not recording.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_271

LANGUAGE: APIDOC
CODE:
```
Method: ToggleRecord
Description: Toggles the status of the record output.
Details:
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
Response Fields:
  outputActive (Boolean): The new active state of the output
```

----------------------------------------

TITLE: Offset Media Input Cursor API
DESCRIPTION: Adjusts the current playback cursor position of a media input by a specified offset value. This request does not perform bounds checking.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_281

LANGUAGE: APIDOC
CODE:
```
Method: OffsetMediaInputCursor
Description: Offsets the current cursor position of a media input by the specified value.
This request does not perform bounds checking of the cursor position.
Details:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
Request Fields:
  ?inputName (String): Name of the media input (Value Restrictions: None, Default Behavior: Unknown)
  ?inputUuid (String): UUID of the media input (Value Restrictions: None, Default Behavior: Unknown)
  mediaCursorOffset (Number): Value to offset the current cursor position by (Value Restrictions: None, Default Behavior: N/A)
```

----------------------------------------

TITLE: RequestStatus::RequestProcessingFailed
DESCRIPTION: Processing the request failed unexpectedly. A comment is required to be provided by obs-websocket.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_54

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 702
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: RequestBatchResponse (OpCode 9) API Definition
DESCRIPTION: Defines the structure for obs-websocket's response to a client's batch request. It includes the original `requestId` and an array of `results` corresponding to the processed requests.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_15

LANGUAGE: APIDOC
CODE:
```
RequestBatchResponse (OpCode 9)
  Sent from: obs-websocket
  Sent to: Identified client which made the request
  Description: obs-websocket is responding to a request batch coming from the client.
  Data Keys:
    requestId: string
    results: array<object>
```

----------------------------------------

TITLE: GetSceneItemSource API Reference
DESCRIPTION: Retrieves the source associated with a specific scene item, identified by its numeric ID within a scene.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_234

LANGUAGE: APIDOC
CODE:
```
GetSceneItemSource:
  Request Fields:
    ?sceneName: String - Name of the scene the item is in
    ?sceneUuid: String - UUID of the scene the item is in
    sceneItemId: Number - Numeric ID of the scene item
  Response Fields:
    sourceName: String - Name of the source associated with the scene item
    sourceUuid: String - UUID of the source associated with the scene item
```

----------------------------------------

TITLE: EventSubscription::Filters
DESCRIPTION: Subscription value to receive events in the `Filters` category.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_62

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 5)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: RequestStatus::InvalidResourceType Error Code
DESCRIPTION: The type of resource found is invalid.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_46

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 602
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: CurrentSceneTransitionChanged Event
DESCRIPTION: Documents the 'CurrentSceneTransitionChanged' event, which signifies that the active scene transition has been updated. It provides the name and UUID of the new transition.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_108

LANGUAGE: APIDOC
CODE:
```
Event: CurrentSceneTransitionChanged
Description: The current scene transition has changed.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  transitionName: String - Name of the new transition
  transitionUuid: String - UUID of the new transition
```

----------------------------------------

TITLE: RequestStatus Enumeration
DESCRIPTION: Provides a comprehensive list of status codes returned by OBS-WebSocket requests, indicating success, various errors, or specific state conditions.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_19

LANGUAGE: APIDOC
CODE:
```
RequestStatus:
  Unknown
  NoError
  Success
  MissingRequestType
  UnknownRequestType
  GenericError
  UnsupportedRequestBatchExecutionType
  NotReady
  MissingRequestField
  MissingRequestData
  InvalidRequestField
  InvalidRequestFieldType
  RequestFieldOutOfRange
  RequestFieldEmpty
  TooManyRequestFields
  OutputRunning
  OutputNotRunning
  OutputPaused
  OutputNotPaused
  OutputDisabled
  StudioModeActive
  StudioModeNotActive
  ResourceNotFound
  ResourceAlreadyExists
  InvalidResourceType
  NotEnoughResources
  InvalidResourceState
  InvalidInputKind
  ResourceNotConfigurable
  InvalidFilterKind
  ResourceCreationFailed
  ResourceActionFailed
  RequestProcessingFailed
  CannotAct
```

----------------------------------------

TITLE: OBS WebSocket Request Status Codes
DESCRIPTION: Lists various status codes returned by OBS WebSocket requests, indicating success, failure, or specific error conditions.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_28

LANGUAGE: APIDOC
CODE:
```
RequestStatus::Unknown
  Description: Unknown status, should never be used.
  Identifier Value: 0
  Latest Supported RPC Version: 1
  Added in: v5.0.0

RequestStatus::NoError
  Description: For internal use to signify a successful field check.
  Identifier Value: 10
  Latest Supported RPC Version: 1
  Added in: v5.0.0

RequestStatus::Success
  Description: The request has succeeded.
  Identifier Value: 100
  Latest Supported RPC Version: 1
  Added in: v5.0.0

RequestStatus::MissingRequestType
  Description: The `requestType` field is missing from the request data.
  Identifier Value: 203
  Latest Supported RPC Version: 1
  Added in: v5.0.0

RequestStatus::UnknownRequestType
  Description: The request type is invalid or does not exist.
  Identifier Value: 204
  Latest Supported RPC Version: 1
  Added in: v5.0.0

RequestStatus::GenericError
  Description: Generic error code. Note: A comment is required to be provided by obs-websocket.
  Identifier Value: 205
  Latest Supported RPC Version: 1
  Added in: v5.0.0

RequestStatus::UnsupportedRequestBatchExecutionType
  Description: The request batch execution type is not supported.
  Identifier Value: 206
  Latest Supported RPC Version: 1
  Added in: v5.0.0
```

----------------------------------------

TITLE: API Event: InputVolumeChanged (OBS-websocket)
DESCRIPTION: Documents the 'InputVolumeChanged' event, which occurs when an input's volume level is adjusted. It provides the input's name, UUID, and both the new volume level multiplier and the new volume level in dB.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_102

LANGUAGE: APIDOC
CODE:
```
Event: InputVolumeChanged
Description: An input's volume level has changed.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
- inputVolumeMul: Number (New volume level multiplier)
- inputVolumeDb: Number (New volume level in dB)
```

----------------------------------------

TITLE: OBS-WebSocket: CurrentPreviewSceneChanged Event
DESCRIPTION: This event is emitted when the current preview scene in OBS has changed. It provides the name and UUID of the scene that is now in preview.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_93

LANGUAGE: APIDOC
CODE:
```
Event: CurrentPreviewSceneChanged
Description: The current preview scene has changed.
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  sceneName: String - Name of the scene that was switched to
  sceneUuid: String - UUID of the scene that was switched to
```

----------------------------------------

TITLE: Set Input Deinterlace Mode API Documentation
DESCRIPTION: Sets the deinterlace mode of an input. Deinterlacing functionality is restricted to async inputs only. This API endpoint is part of OBS-websocket, supports RPC Version 1, and was added in v5.6.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_207

LANGUAGE: APIDOC
CODE:
```
SetInputDeinterlaceMode:
  Description: Sets the deinterlace mode of an input.
  Details:
    Notes: Deinterlacing functionality is restricted to async inputs only.
    Complexity Rating: 2/5
    Latest Supported RPC Version: 1
    Added in: v5.6.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputDeinterlaceMode:
      Type: String
      Description: Deinterlace mode for the input
      Value Restrictions: None
      Default Behavior: N/A
      Optional: false
```

----------------------------------------

TITLE: SceneItemListReindexed Event
DESCRIPTION: A scene's item list has been reindexed. This event has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_121

LANGUAGE: APIDOC
CODE:
```
Event: SceneItemListReindexed
Description: A scene's item list has been reindexed.
Parameters:
  sceneName (String): Name of the scene
  sceneUuid (String): UUID of the scene
  sceneItems (Array<Object>): Array of scene item objects
```

----------------------------------------

TITLE: Toggle Input Mute State (OBS WebSocket API)
DESCRIPTION: Toggles the audio mute state of an input. This API endpoint has a complexity rating of 2/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_195

LANGUAGE: APIDOC
CODE:
```
ToggleInputMute:
  Description: Toggles the audio mute state of an input.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input to toggle the mute state of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input to toggle the mute state of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
  Response Fields:
    inputMuted:
      Type: Boolean
      Description: Whether the input has been muted or unmuted
```

----------------------------------------

TITLE: SetSceneItemTransform API Method
DESCRIPTION: Sets the transform and crop information of a scene item. This method allows precise control over the position, rotation, scale, and cropping of individual items within an OBS scene.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_239

LANGUAGE: APIDOC
CODE:
```
Method: SetSceneItemTransform
Description: Sets the transform and crop info of a scene item.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in: v5.0.0
Request Fields:
  - Name: ?sceneName, Type: String, Description: Name of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: ?sceneUuid, Type: String, Description: UUID of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: sceneItemId, Type: Number, Description: Numeric ID of the scene item, Value Restrictions: >= 0, Default Behavior: N/A
  - Name: sceneItemTransform, Type: Object, Description: Object containing scene item transform info to update, Value Restrictions: None, Default Behavior: N/A
```

----------------------------------------

TITLE: Remove Input API Documentation
DESCRIPTION: Removes an existing input from OBS. Note that this action will immediately remove all associated scene items linked to the input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_188

LANGUAGE: APIDOC
CODE:
```
RemoveInput:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - inputName (String): Name of the input to remove. Value Restrictions: None. Default Behavior: Unknown.
    - inputUuid (String): UUID of the input to remove. Value Restrictions: None. Default Behavior: Unknown.
```

----------------------------------------

TITLE: Split Record File API
DESCRIPTION: Splits the current recording into a new file without stopping the recording process.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_277

LANGUAGE: APIDOC
CODE:
```
Method: SplitRecordFile
Description: Splits the current file being recorded into a new file.
Details:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.5.0
```

----------------------------------------

TITLE: RequestBatch (OpCode 8) API Definition
DESCRIPTION: Defines the structure for a client-initiated batch of requests sent to obs-websocket. Requests are processed serially, with an option to halt on the first failure. The `requests` array contains individual request payloads.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_13

LANGUAGE: APIDOC
CODE:
```
RequestBatch (OpCode 8):
  Sent from: Identified client
  Sent to: obs-websocket
  Description: Client is making a batch of requests for obs-websocket. Requests are processed serially (in order) by the server.
  Data Keys:
    {
      "requestId": string,
      "haltOnFailure": bool(optional) = false,
      "executionType": number(optional) = RequestBatchExecutionType::SerialRealtime,
      "requests": array<object>
    }
  Notes:
    - When `haltOnFailure` is `true`, the processing of requests will be halted on first failure. Returns only the processed requests in `RequestBatchResponse`.
    - Requests in the `requests` array follow the same structure as the `Request` payload data format, however `requestId` is an optional field.
```

----------------------------------------

TITLE: SetProfileParameter
DESCRIPTION: Sets the value of a parameter in the current profile's configuration.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_163

LANGUAGE: APIDOC
CODE:
```
Method: SetProfileParameter
Complexity Rating: 4/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  parameterCategory: String - Category of the parameter to set
  parameterName: String - Name of the parameter to set
  parameterValue: String - Value of the parameter to set. Use null to delete
```

----------------------------------------

TITLE: RequestBatch (OpCode 8) API Definition
DESCRIPTION: Defines the structure for clients to send a batch of requests to obs-websocket. Requests are processed serially. The `haltOnFailure` flag determines if processing stops on the first error, and `executionType` specifies how requests are executed. The `requests` array contains individual request payloads.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_14

LANGUAGE: APIDOC
CODE:
```
RequestBatch (OpCode 8)
  Sent from: Identified client
  Sent to: obs-websocket
  Description: Client is making a batch of requests for obs-websocket. Requests are processed serially (in order) by the server.
  Data Keys:
    requestId: string
    haltOnFailure: bool (optional, default: false)
    executionType: number (optional, default: RequestBatchExecutionType::SerialRealtime)
    requests: array<object>
  Notes:
    - When haltOnFailure is true, the processing of requests will be halted on first failure. Returns only the processed requests in RequestBatchResponse.
    - Requests in the 'requests' array follow the same structure as the Request payload data format, however requestId is an optional field.
```

----------------------------------------

TITLE: InputVolumeMeters Event
DESCRIPTION: Documents the 'InputVolumeMeters' event, a high-volume event that provides real-time volume levels for all active inputs. This event is emitted every 50 milliseconds.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_107

LANGUAGE: APIDOC
CODE:
```
Event: InputVolumeMeters
Description: A high-volume event providing volume levels of all active inputs every 50 milliseconds.
Complexity Rating: 4/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  inputs: Array<Object> - Array of active inputs with their associated volume levels
```

----------------------------------------

TITLE: InputAudioMonitorTypeChanged Event
DESCRIPTION: Documents the 'InputAudioMonitorTypeChanged' event, which is triggered when an input's audio monitor type changes. It includes details on available monitor types and the data fields provided with the event.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_106

LANGUAGE: APIDOC
CODE:
```
Event: InputAudioMonitorTypeChanged
Description: The monitor type of an input has changed.
Available types are:
- OBS_MONITORING_TYPE_NONE
- OBS_MONITORING_TYPE_MONITOR_ONLY
- OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  inputName: String - Name of the input
  inputUuid: String - UUID of the input
  monitorType: String - New monitor type of the input
```

----------------------------------------

TITLE: WebSocketOpCode Enumeration
DESCRIPTION: Defines the operation codes used for WebSocket communication within OBS-WebSocket, indicating the type of message being sent or received.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_16

LANGUAGE: APIDOC
CODE:
```
WebSocketOpCode:
  Hello
  Identify
  Identified
  Reidentify
  Event
  Request
  RequestResponse
  RequestBatch
  RequestBatchResponse
```

----------------------------------------

TITLE: API Event: InputAudioBalanceChanged (OBS-websocket)
DESCRIPTION: Documents the 'InputAudioBalanceChanged' event, triggered when an input's audio balance value is modified. It includes the input's name, UUID, and the new audio balance value.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_103

LANGUAGE: APIDOC
CODE:
```
Event: InputAudioBalanceChanged
Description: The audio balance value of an input has changed.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
- inputAudioBalance: Number (New audio balance value of the input)
```

----------------------------------------

TITLE: Toggle Output Status API for OBS WebSocket
DESCRIPTION: Toggles the active status of a specified OBS output. Requires the output name as input and returns the new active state.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_260

LANGUAGE: APIDOC
CODE:
```
ToggleOutput:
  Request:
    outputName: String - Output name
  Response:
    outputActive: Boolean - Whether the output is active
```

----------------------------------------

TITLE: ObsMediaInputAction::OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PAUSE
DESCRIPTION: Pause the media input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_75

LANGUAGE: APIDOC
CODE:
```
Identifier Value: OBS_WEBSOCKET_MEDIA_INPUT_ACTION_PAUSE
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: SceneItemLockStateChanged Event
DESCRIPTION: A scene item's lock state has changed. This event has a complexity rating of 3/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_123

LANGUAGE: APIDOC
CODE:
```
Event: SceneItemLockStateChanged
Description: A scene item's lock state has changed.
Parameters:
  sceneName (String): Name of the scene the item is in
  sceneUuid (String): UUID of the scene the item is in
  sceneItemId (Number): Numeric ID of the scene item
  sceneItemLocked (Boolean): Whether the scene item is locked
```

----------------------------------------

TITLE: Reidentify (OpCode 3)
DESCRIPTION: Sent at any time after initial identification to update the provided session parameters.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/docs/partials/introduction.md#_snippet_10

LANGUAGE: APIDOC
CODE:
```
Sent from: Identified client
Sent to: obs-websocket

Data Keys:
{
  "eventSubscriptions": number(optional) = (EventSubscription::All)
}
  Only the listed parameters may be changed after initial identification. To change a parameter not listed, you must reconnect to the obs-websocket server.
```

----------------------------------------

TITLE: ObsMediaInputAction::OBS_WEBSOCKET_MEDIA_INPUT_ACTION_STOP
DESCRIPTION: Stop the media input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_76

LANGUAGE: APIDOC
CODE:
```
Identifier Value: OBS_WEBSOCKET_MEDIA_INPUT_ACTION_STOP
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: StudioModeStateChanged Event
DESCRIPTION: This event is triggered when Studio Mode is enabled or disabled. It provides a boolean indicating the current state of Studio Mode. This event was added in v5.0.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_135

LANGUAGE: APIDOC
CODE:
```
Event: StudioModeStateChanged
Properties:
  - studioModeEnabled: Boolean (True == Enabled, False == Disabled)
```

----------------------------------------

TITLE: RequestStatus::InvalidFilterKind Error Code
DESCRIPTION: The specified filter (obs_source_t-OBS_SOURCE_TYPE_FILTER) had the wrong kind.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_51

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 607
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: OBS-WebSocket: ProfileListChanged Event
DESCRIPTION: This event is emitted when the list of available OBS profiles has been updated. This includes scenarios where profiles are added, removed, or reordered.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_88

LANGUAGE: APIDOC
CODE:
```
Event: ProfileListChanged
Description: The profile list has changed.
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  profiles: Array<String> - Updated list of profiles
```

----------------------------------------

TITLE: Send Stream Caption API for OBS WebSocket
DESCRIPTION: Sends CEA-608 caption text over the OBS stream output. Requires the caption text as input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_269

LANGUAGE: APIDOC
CODE:
```
SendStreamCaption:
  Request:
    captionText: String - Caption text
  Response: None
```

----------------------------------------

TITLE: EventSubscription::InputShowStateChanged
DESCRIPTION: Subscription value to receive the `InputShowStateChanged` high-volume event.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_71

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 18)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Set Input Mute State (OBS WebSocket API)
DESCRIPTION: Sets the audio mute state of an input. This API endpoint has a complexity rating of 2/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_194

LANGUAGE: APIDOC
CODE:
```
SetInputMute:
  Description: Sets the audio mute state of an input.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input to set the mute state of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input to set the mute state of
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputMuted:
      Type: Boolean
      Description: Whether to mute the input or not
      Value Restrictions: None
      Default Behavior: N/A
```

----------------------------------------

TITLE: Document OBS-websocket CustomEvent
DESCRIPTION: Documents the `CustomEvent`, which is emitted by the `BroadcastCustomEvent` function. This event carries custom data defined by the broadcaster.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_82

LANGUAGE: APIDOC
CODE:
```
CustomEvent:
  Description: Custom event emitted by `BroadcastCustomEvent`.
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Data Fields:
    eventData: Object - Custom event data
```

----------------------------------------

TITLE: EventSubscription::InputActiveStateChanged
DESCRIPTION: Subscription value to receive the `InputActiveStateChanged` high-volume event.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_70

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 17)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: OBS-WebSocket: CurrentProgramSceneChanged Event
DESCRIPTION: This event signifies that the active program scene in OBS has changed. It provides the name and UUID of the scene that is now live.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_92

LANGUAGE: APIDOC
CODE:
```
Event: CurrentProgramSceneChanged
Description: The current program scene has changed.
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  sceneName: String - Name of the scene that was switched to
  sceneUuid: String - UUID of the scene that was switched to
```

----------------------------------------

TITLE: RequestStatus::MissingRequestField Error Code
DESCRIPTION: A required request field is missing.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_30

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 300
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: RequestBatchResponse (OpCode 9) API Definition
DESCRIPTION: Defines the response structure from obs-websocket to a client's request batch. It includes the original `requestId` and an array of `results` for each processed request.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_14

LANGUAGE: APIDOC
CODE:
```
RequestBatchResponse (OpCode 9):
  Sent from: obs-websocket
  Sent to: Identified client which made the request
  Description: obs-websocket is responding to a request batch coming from the client.
  Data Keys:
    {
      "requestId": string,
      "results": array<object>
    }
```

----------------------------------------

TITLE: RequestResponse (OpCode 7)
DESCRIPTION: This message is sent from obs-websocket back to the identified client that initiated a request. It serves as the response to a client's request, mirroring the `requestType` and `requestId` from the original request. The `requestStatus` object indicates the outcome, with `result` being true for success, `code` providing a `RequestStatus` code, and an optional `comment` for error details.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_12

LANGUAGE: txt
CODE:
```
{
  "requestType": string,
  "requestId": string,
  "requestStatus": object,
  "responseData": object(optional)
}
```

LANGUAGE: txt
CODE:
```
{
  "result": bool,
  "code": number,
  "comment": string(optional)
}
```

LANGUAGE: json
CODE:
```
{
  "op": 7,
  "d": {
    "requestType": "SetCurrentProgramScene",
    "requestId": "f819dcf0-89cc-11eb-8f0e-382c4ac93b9c",
    "requestStatus": {
      "result": true,
      "code": 100
    }
  }
}
```

LANGUAGE: json
CODE:
```
{
  "op": 7,
  "d": {
    "requestType": "SetCurrentProgramScene",
    "requestId": "f819dcf0-89cc-11eb-8f0e-382c4ac93b9c",
    "requestStatus": {
      "result": false,
      "code": 608,
      "comment": "Parameter: sceneName"
    }
  }
}
```

----------------------------------------

TITLE: RequestStatus::TooManyRequestFields Error Code
DESCRIPTION: There are too many request fields (eg. a request takes two optionals, where only one is allowed at a time).

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_36

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 404
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Remove Scene (OBS-WebSocket API)
DESCRIPTION: Removes a scene from OBS.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_180

LANGUAGE: APIDOC
CODE:
```
RemoveScene
  Description: Removes a scene from OBS.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    ?sceneName: String - Name of the scene to remove (Value Restrictions: None, Default Behavior: Unknown)
    ?sceneUuid: String - UUID of the scene to remove (Value Restrictions: None, Default Behavior: Unknown)
```

----------------------------------------

TITLE: API Event: InputShowStateChanged (OBS-websocket)
DESCRIPTION: Documents the 'InputShowStateChanged' event, which signifies a change in an input's show state. An input is showing when it's visible in the preview or a dialog. The event provides the input's name, UUID, and its new showing state.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_100

LANGUAGE: APIDOC
CODE:
```
Event: InputShowStateChanged
Description: An input's show state has changed.
When an input is showing, it means it's being shown by the preview or a dialog.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
- videoShowing: Boolean (Whether the input is showing)
```

----------------------------------------

TITLE: API Event: InputAudioTracksChanged (OBS-websocket)
DESCRIPTION: Documents the 'InputAudioTracksChanged' event, triggered when the audio tracks associated with an input are modified. It includes the input's name, UUID, and an object detailing the audio tracks along with their enabled states.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_105

LANGUAGE: APIDOC
CODE:
```
Event: InputAudioTracksChanged
Description: The audio tracks of an input have changed.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
- inputAudioTracks: Object (Object of audio tracks along with their associated enable states)
```

----------------------------------------

TITLE: EventSubscription::SceneItemTransformChanged
DESCRIPTION: Subscription value to receive the `SceneItemTransformChanged` high-volume event.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_72

LANGUAGE: APIDOC
CODE:
```
Identifier Value: (1 << 19)
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: SceneItemTransformChanged Event
DESCRIPTION: The transform/crop of a scene item has changed. This event has a complexity rating of 4/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_125

LANGUAGE: APIDOC
CODE:
```
Event: SceneItemTransformChanged
Description: The transform/crop of a scene item has changed.
Parameters:
  sceneName (String): The name of the scene the item is in
  sceneUuid (String): The UUID of the scene the item is in
  sceneItemId (Number): Numeric ID of the scene item
  sceneItemTransform (Object): New transform/crop info of the scene item
```

----------------------------------------

TITLE: WebSocketCloseCode Enumeration
DESCRIPTION: Specifies the various close codes that can be sent by the OBS-WebSocket server to indicate the reason for a connection termination.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_17

LANGUAGE: APIDOC
CODE:
```
WebSocketCloseCode:
  DontClose
  UnknownReason
  MessageDecodeError
  MissingDataField
  InvalidDataFieldType
  InvalidDataFieldValue
  UnknownOpCode
  NotIdentified
  AlreadyIdentified
  AuthenticationFailed
  UnsupportedRpcVersion
  SessionInvalidated
  UnsupportedFeature
```

----------------------------------------

TITLE: Stop Output API for OBS WebSocket
DESCRIPTION: Halts a specified OBS output. Requires the output name as input.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_262

LANGUAGE: APIDOC
CODE:
```
StopOutput:
  Request:
    outputName: String - Output name
  Response: None
```

----------------------------------------

TITLE: Set Scene Item Blend Mode (OBS-Websocket API)
DESCRIPTION: Sets the blend mode for a specific scene item. This method requires the scene item's ID and the desired new blend mode. It supports various blend modes like normal, additive, and multiply.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_247

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  ?sceneName: String - Name of the scene the item is in (Value Restrictions: None, Default Behavior: Unknown)
  ?sceneUuid: String - UUID of the scene the item is in (Value Restrictions: None, Default Behavior: Unknown)
  sceneItemId: Number - Numeric ID of the scene item (Value Restrictions: >= 0, Default Behavior: N/A)
  sceneItemBlendMode: String - New blend mode (Value Restrictions: None, Default Behavior: N/A)
```

----------------------------------------

TITLE: OBS WebSocket Close Codes
DESCRIPTION: Defines various close codes used by the OBS WebSocket protocol, indicating reasons for connection termination.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_26

LANGUAGE: APIDOC
CODE:
```
WebSocketCloseCode::MessageDecodeError
  Description: The server was unable to decode the incoming websocket message.
  Identifier Value: 4002
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::MissingDataField
  Description: A data field is required but missing from the payload.
  Identifier Value: 4003
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::InvalidDataFieldType
  Description: A data field's value type is invalid.
  Identifier Value: 4004
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::InvalidDataFieldValue
  Description: A data field's value is invalid.
  Identifier Value: 4005
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::UnknownOpCode
  Description: The specified `op` was invalid or missing.
  Identifier Value: 4006
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::NotIdentified
  Description: The client sent a websocket message without first sending `Identify` message.
  Identifier Value: 4007
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::AlreadyIdentified
  Description: The client sent an `Identify` message while already identified. Note: Once a client has identified, only `Reidentify` may be used to change session parameters.
  Identifier Value: 4008
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::AuthenticationFailed
  Description: The authentication attempt (via `Identify`) failed.
  Identifier Value: 4009
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::UnsupportedRpcVersion
  Description: The server detected the usage of an old version of the obs-websocket RPC protocol.
  Identifier Value: 4010
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::SessionInvalidated
  Description: The websocket session has been invalidated by the obs-websocket server. Note: This is the code used by the `Kick` button in the UI Session List. If you receive this code, you must not automatically reconnect.
  Identifier Value: 4011
  Latest Supported RPC Version: 1
  Added in: v5.0.0

WebSocketCloseCode::UnsupportedFeature
  Description: A requested feature is not supported due to hardware/software limitations.
  Identifier Value: 4012
  Latest Supported RPC Version: 1
  Added in: v5.0.0
```

----------------------------------------

TITLE: RequestStatus::RequestFieldEmpty Error Code
DESCRIPTION: A request field (string or array) is empty and cannot be.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_35

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 403
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Stop Virtual Camera Output (OBS-Websocket API)
DESCRIPTION: Halts the virtual camera output. This command deactivates the virtual camera.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_251

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: RequestStatus::MissingRequestData Error Code
DESCRIPTION: The request does not have a valid requestData object.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_31

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 301
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: VirtualcamStateChanged Event
DESCRIPTION: This event is triggered when the state of the virtual camera output changes. It provides information about whether the virtual camera is active and its specific state. This event was added in v5.0.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_130

LANGUAGE: APIDOC
CODE:
```
Event: VirtualcamStateChanged
Properties:
  - outputActive: Boolean (Whether the output is active)
  - outputState: String (The specific state of the output)
```

----------------------------------------

TITLE: OBS-WebSocket: CurrentProfileChanged Event
DESCRIPTION: This event signals that the current OBS profile has successfully changed. It provides the name of the newly active profile.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_87

LANGUAGE: APIDOC
CODE:
```
Event: CurrentProfileChanged
Description: The current profile has changed.
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  profileName: String - Name of the new profile
```

----------------------------------------

TITLE: SceneTransitionVideoEnded Event
DESCRIPTION: Documents the 'SceneTransitionVideoEnded' event, indicating that the video component of a scene transition has finished playing. This is particularly useful for stinger transitions to determine the actual end of the video playback, distinct from the cut point signified by 'SceneTransitionEnded'.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_112

LANGUAGE: APIDOC
CODE:
```
Event: SceneTransitionVideoEnded
Description: A scene transition's video has completed fully.
Useful for stinger transitions to tell when the video *actually* ends.
`SceneTransitionEnded` only signifies the cut point, not the completion of transition playback.
Note: Appears to be called by every transition, regardless of relevance.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  transitionName: String - Scene transition name
  transitionUuid: String - Scene transition UUID
```

----------------------------------------

TITLE: Set Input Deinterlace Field Order API Documentation
DESCRIPTION: Sets the deinterlace field order of an input. Deinterlacing functionality is restricted to async inputs only. This API endpoint is part of OBS-websocket, supports RPC Version 1, and was added in v5.6.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_209

LANGUAGE: APIDOC
CODE:
```
SetInputDeinterlaceFieldOrder:
  Description: Sets the deinterlace field order of an input.
  Details:
    Notes: Deinterlacing functionality is restricted to async inputs only.
    Complexity Rating: 2/5
    Latest Supported RPC Version: 1
    Added in: v5.6.0
  Request Fields:
    inputName:
      Type: String
      Description: Name of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputUuid:
      Type: String
      Description: UUID of the input
      Value Restrictions: None
      Default Behavior: Unknown
      Optional: true
    inputDeinterlaceFieldOrder:
      Type: String
      Description: Deinterlace field order for the input
      Value Restrictions: None
      Default Behavior: N/A
      Optional: false
```

----------------------------------------

TITLE: SetStreamServiceSettings
DESCRIPTION: Sets the current stream service settings (stream destination). Note: Simple RTMP settings can be set with type rtmp_custom and the settings fields server and key.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_167

LANGUAGE: APIDOC
CODE:
```
Method: SetStreamServiceSettings
Complexity Rating: 4/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  streamServiceType: String - Type of stream service to apply. Example: rtmp_common or rtmp_custom
  streamServiceSettings: Object - Settings to apply to the service
```

----------------------------------------

TITLE: RequestStatus::OutputDisabled Error Code
DESCRIPTION: An output is disabled and should not be.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_41

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 504
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: SetInputAudioMonitorType API Method
DESCRIPTION: Sets the audio monitor type of an input. Valid types include 'OBS_MONITORING_TYPE_NONE', 'OBS_MONITORING_TYPE_MONITOR_ONLY', and 'OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT'.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_203

LANGUAGE: APIDOC
CODE:
```
SetInputAudioMonitorType:
  Description: Sets the audio monitor type of an input.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - Name: inputName (Optional)
      Type: String
      Description: Name of the input to set the audio monitor type of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: inputUuid (Optional)
      Type: String
      Description: UUID of the input to set the audio monitor type of
      Value Restrictions: None
      Default Behavior: Unknown
    - Name: monitorType
      Type: String
      Description: Audio monitor type
      Value Restrictions: None
      Default Behavior: N/A
```

----------------------------------------

TITLE: Set Source Filter Index Position API
DESCRIPTION: Adjusts the display order of a filter on a source by setting its new index position. The provided index must be a non-negative number. The source can be identified by name or UUID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_228

LANGUAGE: APIDOC
CODE:
```
SetSourceFilterIndex:
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    ?sourceName: String - Name of the source the filter is on
    ?sourceUuid: String - UUID of the source the filter is on
    filterName: String - Name of the filter
    filterIndex: Number - New index position of the filter (>= 0)
```

----------------------------------------

TITLE: Stop Record Output API
DESCRIPTION: Halts the recording process for the OBS record output and provides the path to the saved file.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_273

LANGUAGE: APIDOC
CODE:
```
Method: StopRecord
Description: Stops the record output.
Details:
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
Response Fields:
  outputPath (String): File name for the saved recording
```

----------------------------------------

TITLE: EventSubscription::None
DESCRIPTION: Subscription value used to disable all events.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_56

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 0
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: SceneTransitionEnded Event
DESCRIPTION: Documents the 'SceneTransitionEnded' event, which signals that a scene transition has fully completed. Note that this event may not trigger if the transition is interrupted by the user.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_111

LANGUAGE: APIDOC
CODE:
```
Event: SceneTransitionEnded
Description: A scene transition has completed fully.
Note: Does not appear to trigger when the transition is interrupted by the user.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  transitionName: String - Scene transition name
  transitionUuid: String - Scene transition UUID
```

----------------------------------------

TITLE: ReplayBufferSaved Event
DESCRIPTION: This event is triggered when the replay buffer has been successfully saved. It provides the file path of the saved replay. This event was added in v5.0.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_131

LANGUAGE: APIDOC
CODE:
```
Event: ReplayBufferSaved
Properties:
  - savedReplayPath: String (Path of the saved replay file)
```

----------------------------------------

TITLE: Toggle Stream Status API for OBS WebSocket
DESCRIPTION: Toggles the active status of the OBS stream output. Returns the new active state of the stream.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_266

LANGUAGE: APIDOC
CODE:
```
ToggleStream:
  Request: None
  Response:
    outputActive: Boolean - New state of the stream output
```

----------------------------------------

TITLE: OBS-WebSocket: SceneListChanged Event
DESCRIPTION: This event indicates that the overall list of scenes in OBS has been modified. This includes additions, removals, or reordering of scenes. A TODO note indicates that OBS should fire this event when scenes are reordered.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_94

LANGUAGE: APIDOC
CODE:
```
Event: SceneListChanged
Description: The list of scenes has changed.
TODO: Make OBS fire this event when scenes are reordered.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  scenes: Array<Object> - Updated array of scenes
```

----------------------------------------

TITLE: RequestStatus::OutputNotPaused Error Code
DESCRIPTION: An output is not paused and should be.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_40

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 503
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: RemoveProfile API Method
DESCRIPTION: Removes a specified profile. If the profile being removed is currently active, OBS will automatically switch to a different profile first.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_161

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  - profileName: String - Name of the profile to remove
```

----------------------------------------

TITLE: SetCurrentSceneTransitionDuration
DESCRIPTION: Sets the duration of the current scene transition, if it is not fixed.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_216

LANGUAGE: APIDOC
CODE:
```
SetCurrentSceneTransitionDuration:
  Description: Sets the duration of the current scene transition, if it is not fixed.
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
  Request Fields:
    - transitionDuration (Number): Duration in milliseconds [Value Restrictions: >= 50, <= 20000] [Default Behavior: N/A]
```

----------------------------------------

TITLE: CurrentSceneTransitionDurationChanged Event
DESCRIPTION: Documents the 'CurrentSceneTransitionDurationChanged' event, indicating a change in the duration of the current scene transition. The event provides the new duration in milliseconds.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_109

LANGUAGE: APIDOC
CODE:
```
Event: CurrentSceneTransitionDurationChanged
Description: The current scene transition duration has changed.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  transitionDuration: Number - Transition duration in milliseconds
```

----------------------------------------

TITLE: OBS-WebSocket: SceneNameChanged Event
DESCRIPTION: This event is triggered when the name of an existing scene has been modified. It provides both the old and new names of the scene, along with its UUID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_91

LANGUAGE: APIDOC
CODE:
```
Event: SceneNameChanged
Description: The name of a scene has changed.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  sceneUuid: String - UUID of the scene
  oldSceneName: String - Old name of the scene
  sceneName: String - New name of the scene
```

----------------------------------------

TITLE: API Event: InputNameChanged (OBS-websocket)
DESCRIPTION: Documents the 'InputNameChanged' event, which is triggered when an input's name is updated. It includes the input's UUID, its old name, and its new name.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_97

LANGUAGE: APIDOC
CODE:
```
Event: InputNameChanged
Description: The name of an input has changed.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputUuid: String (UUID of the input)
- oldInputName: String (Old name of the input)
- inputName: String (New name of the input)
```

----------------------------------------

TITLE: SourceFilterNameChanged Event
DESCRIPTION: Documents the 'SourceFilterNameChanged' event, indicating that the name of a source filter has been modified. It includes the source name, the old filter name, and the new filter name.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_116

LANGUAGE: APIDOC
CODE:
```
Event: SourceFilterNameChanged
Description: The name of a source filter has changed.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  sourceName: String - The source the filter is on
  oldFilterName: String - Old name of the filter
  filterName: String - New name of the filter
```

----------------------------------------

TITLE: ReplayBufferStateChanged Event
DESCRIPTION: This event is triggered when the state of the replay buffer output changes. It provides information about whether the replay buffer is active and its specific state. This event was added in v5.0.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_129

LANGUAGE: APIDOC
CODE:
```
Event: ReplayBufferStateChanged
Properties:
  - outputActive: Boolean (Whether the output is active)
  - outputState: String (The specific state of the output)
```

----------------------------------------

TITLE: RequestStatus::InvalidRequestField Error Code
DESCRIPTION: Generic invalid request field message. A comment is required to be provided by obs-websocket.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_32

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 400
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Reidentify (OpCode 3)
DESCRIPTION: This message can be sent at any time after initial identification from an identified client to obs-websocket. Its purpose is to update the provided session parameters. Only the listed parameters, such as `eventSubscriptions`, may be changed after initial identification; to change other parameters, a reconnection to the obs-websocket server is required.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_9

LANGUAGE: txt
CODE:
```
{
  "eventSubscriptions": number(optional) = (EventSubscription::All)
}
```

----------------------------------------

TITLE: Stop Replay Buffer Output (OBS-Websocket API)
DESCRIPTION: Halts the replay buffer output. This command deactivates the replay buffer.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_255

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: Remove Source Filter
DESCRIPTION: Removes a filter from a specified source.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_225

LANGUAGE: APIDOC
CODE:
```
RemoveSourceFilter:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    sourceName: String - Name of the source the filter is on (Optional).
    sourceUuid: String - UUID of the source the filter is on (Optional).
    filterName: String - Name of the filter to remove.
```

----------------------------------------

TITLE: API Event: InputActiveStateChanged (OBS-websocket)
DESCRIPTION: Documents the 'InputActiveStateChanged' event, indicating a change in an input's active state. An input is considered active when it is being shown in the program feed. The event includes the input's name, UUID, and its new active state.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_99

LANGUAGE: APIDOC
CODE:
```
Event: InputActiveStateChanged
Description: An input's active state has changed.
When an input is active, it means it's being shown by the program feed.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
- videoActive: Boolean (Whether the input is active)
```

----------------------------------------

TITLE: Stop Stream API for OBS WebSocket
DESCRIPTION: Halts the OBS stream output.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_268

LANGUAGE: APIDOC
CODE:
```
StopStream:
  Request: None
  Response: None
```

----------------------------------------

TITLE: RecordStateChanged Event
DESCRIPTION: This event is triggered when the state of the record output changes. It provides information about whether the output is active, its specific state, and the path of the saved recording if it has stopped. This event was added in v5.0.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_127

LANGUAGE: APIDOC
CODE:
```
Event: RecordStateChanged
Properties:
  - outputActive: Boolean (Whether the output is active)
  - outputState: String (The specific state of the output)
  - outputPath: String (File name for the saved recording, if record stopped. null otherwise)
```

----------------------------------------

TITLE: Set Source Filter Enabled State API
DESCRIPTION: Toggles the enabled or disabled state of a specific source filter. The source can be identified by name or UUID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_230

LANGUAGE: APIDOC
CODE:
```
SetSourceFilterEnabled:
  Complexity Rating: 3/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    ?sourceName: String - Name of the source the filter is on
    ?sourceUuid: String - UUID of the source the filter is on
    filterName: String - Name of the filter
    filterEnabled: Boolean - New enable state of the filter
```

----------------------------------------

TITLE: SourceFilterListReindexed Event
DESCRIPTION: Documents the 'SourceFilterListReindexed' event, which occurs when the filter list of a source has been reindexed. It provides the source name and the updated array of filter objects.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_113

LANGUAGE: APIDOC
CODE:
```
Event: SourceFilterListReindexed
Description: A source's filter list has been reindexed.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  sourceName: String - Name of the source
  filters: Array<Object> - Array of filter objects
```

----------------------------------------

TITLE: MediaInputPlaybackEnded Event
DESCRIPTION: This event is triggered when a media input finishes playing. It provides the name and UUID of the input that ended playback. This event was added in v5.0.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_133

LANGUAGE: APIDOC
CODE:
```
Event: MediaInputPlaybackEnded
Properties:
  - inputName: String (Name of the input)
  - inputUuid: String (UUID of the input)
```

----------------------------------------

TITLE: Pause Record Output API
DESCRIPTION: Pauses the ongoing recording for the OBS record output.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_275

LANGUAGE: APIDOC
CODE:
```
Method: PauseRecord
Description: Pauses the record output.
Details:
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
```

----------------------------------------

TITLE: StreamStateChanged Event
DESCRIPTION: The state of the stream output has changed. This event has a complexity rating of 2/5, supports RPC Version 1, and was added in v5.0.0.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_126

LANGUAGE: APIDOC
CODE:
```
Event: StreamStateChanged
Description: The state of the stream output has changed.
Parameters:
  outputActive (Boolean): Whether the output is active
  outputState (String): The specific state of the output
```

----------------------------------------

TITLE: RemoveSceneItem API Reference
DESCRIPTION: Removes a specific scene item from a scene, identified by its numeric ID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_236

LANGUAGE: APIDOC
CODE:
```
RemoveSceneItem:
  Request Fields:
    ?sceneName: String - Name of the scene the item is in
    ?sceneUuid: String - UUID of the scene the item is in
    sceneItemId: Number - Numeric ID of the scene item
  Response Fields: None
```

----------------------------------------

TITLE: MediaInputActionTriggered Event
DESCRIPTION: This event is triggered when an action has been performed on a media input. It provides the name and UUID of the input, along with the specific media action that was triggered. Refer to the `ObsMediaInputAction` enum for possible action values. This event was added in v5.0.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_134

LANGUAGE: APIDOC
CODE:
```
Event: MediaInputActionTriggered
Properties:
  - inputName: String (Name of the input)
  - inputUuid: String (UUID of the input)
  - mediaAction: String (Action performed on the input. See ObsMediaInputAction enum)
```

----------------------------------------

TITLE: Toggle Record Pause API
DESCRIPTION: Toggles the pause state of the OBS record output, pausing if active or resuming if paused.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_274

LANGUAGE: APIDOC
CODE:
```
Method: ToggleRecordPause
Description: Toggles pause on the record output.
Details:
  Complexity Rating: 1/5
  Latest Supported RPC Version: 1
  Added in: v5.0.0
```

----------------------------------------

TITLE: ScreenshotSaved Event
DESCRIPTION: This event is triggered when a screenshot has been saved using the built-in screenshot feature (Settings -> Hotkeys -> Screenshot Output). It provides the file path of the saved image. Note: This event is NOT triggered by applications using `Get/SaveSourceScreenshot`. Custom events should be implemented for inter-client communication in such cases. This event was added in v5.1.0 and supports RPC Version 1.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_136

LANGUAGE: APIDOC
CODE:
```
Event: ScreenshotSaved
Properties:
  - savedScreenshotPath: String (Path of the saved image file)
```

----------------------------------------

TITLE: Set Source Filter Name (Rename) API
DESCRIPTION: Sets the name of an existing source filter. This method allows renaming a filter by providing its current name and the desired new name. The source can be identified by either its name or UUID.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_226

LANGUAGE: APIDOC
CODE:
```
SetSourceFilterName:
  Complexity Rating: 2/5
  Latest Supported RPC Version: 1
  Added in v5.0.0
  Request Fields:
    ?sourceName: String - Name of the source the filter is on
    ?sourceUuid: String - UUID of the source the filter is on
    filterName: String - Current name of the filter
    newFilterName: String - New name for the filter
```

----------------------------------------

TITLE: API Event: InputMuteStateChanged (OBS-websocket)
DESCRIPTION: Documents the 'InputMuteStateChanged' event, triggered when an input's mute state changes. It includes the input's name, UUID, and its new mute status.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_101

LANGUAGE: APIDOC
CODE:
```
Event: InputMuteStateChanged
Description: An input's mute state has changed.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
- inputMuted: Boolean (Whether the input is muted)
```

----------------------------------------

TITLE: SetPersistentData API Method
DESCRIPTION: Sets the value of a "slot" from the selected persistent data realm. This method allows storing data by specifying the realm, slot name, and the value to be applied.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_154

LANGUAGE: APIDOC
CODE:
```
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Request Fields:
  - realm: String - The data realm to select. OBS_WEBSOCKET_DATA_REALM_GLOBAL or OBS_WEBSOCKET_DATA_REALM_PROFILE
  - slotName: String - The name of the slot to retrieve data from
  - slotValue: Any - The value to apply to the slot
```

----------------------------------------

TITLE: GetSceneItemLocked API Method
DESCRIPTION: Retrieves the current lock state of a specific scene item. This indicates whether the item is locked in place within scenes or groups, preventing accidental movement or modification.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_242

LANGUAGE: APIDOC
CODE:
```
Method: GetSceneItemLocked
Description: Gets the lock state of a scene item. Scenes and Groups.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in: v5.0.0
Request Fields:
  - Name: ?sceneName, Type: String, Description: Name of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: ?sceneUuid, Type: String, Description: UUID of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: sceneItemId, Type: Number, Description: Numeric ID of the scene item, Value Restrictions: >= 0, Default Behavior: N/A
Response Fields:
  - Name: sceneItemLocked, Type: Boolean, Description: Whether the scene item is locked. true for locked, false for unlocked
```

----------------------------------------

TITLE: RequestStatus::OutputPaused Error Code
DESCRIPTION: An output is paused and should not be.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_39

LANGUAGE: APIDOC
CODE:
```
Identifier Value: 502
Latest Supported RPC Version: 1
Added in v5.0.0
```

----------------------------------------

TITLE: SetSceneItemLocked API Method
DESCRIPTION: Sets the lock state of a specific scene item. This allows locking or unlocking items within scenes and groups to prevent unintended changes.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_243

LANGUAGE: APIDOC
CODE:
```
Method: SetSceneItemLocked
Description: Sets the lock state of a scene item. Scenes and Group.
Complexity Rating: 3/5
Latest Supported RPC Version: 1
Added in: v5.0.0
Request Fields:
  - Name: ?sceneName, Type: String, Description: Name of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: ?sceneUuid, Type: String, Description: UUID of the scene the item is in, Value Restrictions: None, Default Behavior: Unknown
  - Name: sceneItemId, Type: Number, Description: Numeric ID of the scene item, Value Restrictions: >= 0, Default Behavior: N/A
  - Name: sceneItemLocked, Type: Boolean, Description: New lock state of the scene item, Value Restrictions: None, Default Behavior: N/A
```

----------------------------------------

TITLE: SourceFilterRemoved Event
DESCRIPTION: Documents the 'SourceFilterRemoved' event, which is emitted when a filter is removed from a source. It provides the name of the source and the name of the filter that was removed.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_115

LANGUAGE: APIDOC
CODE:
```
Event: SourceFilterRemoved
Description: A filter has been removed from a source.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in: v5.0.0

Data Fields:
  sourceName: String - Name of the source the filter was on
  filterName: String - Name of the filter
```

----------------------------------------

TITLE: API Event: InputRemoved (OBS-websocket)
DESCRIPTION: Documents the 'InputRemoved' event, which is triggered when an input is removed from OBS. It provides the name and UUID of the input that was removed.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_96

LANGUAGE: APIDOC
CODE:
```
Event: InputRemoved
Description: An input has been removed.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
- inputName: String (Name of the input)
- inputUuid: String (UUID of the input)
```

----------------------------------------

TITLE: OBS-WebSocket: SceneCollectionListChanged Event
DESCRIPTION: This event indicates that the list of available scene collections has been modified. This could happen if a new scene collection is created, an existing one is deleted, or their order changes.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_85

LANGUAGE: APIDOC
CODE:
```
Event: SceneCollectionListChanged
Description: The scene collection list has changed.
Complexity Rating: 1/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  sceneCollections: Array<String> - Updated list of scene collections
```

----------------------------------------

TITLE: OBS-WebSocket: SceneRemoved Event
DESCRIPTION: This event indicates that an existing scene has been removed from OBS. It includes information about the deleted scene, such as its name, UUID, and if it was a group.

SOURCE: https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md#_snippet_90

LANGUAGE: APIDOC
CODE:
```
Event: SceneRemoved
Description: A scene has been removed.
Complexity Rating: 2/5
Latest Supported RPC Version: 1
Added in v5.0.0

Data Fields:
  sceneName: String - Name of the removed scene
  sceneUuid: String - UUID of the removed scene
  isGroup: Boolean - Whether the scene was a group
```