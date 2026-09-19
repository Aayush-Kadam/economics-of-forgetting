"""Canonical M6 parameter metadata and predeclared ranges."""

PARAMETER_REGISTRY = {
    "rho": {"symbol":"rho","meaning":"intrinsic quality persistence","default":.55,"bounds":[0,1],"plausible":[.2,.8],"stress":[0,.95],"status":"structural"},
    "alpha": {"symbol":"alpha","meaning":"rehabilitation productivity","default":.55,"bounds":[0,1],"plausible":[.3,.8],"stress":[0,1],"status":"normalized"},
    "kappa": {"symbol":"kappa","meaning":"effort-cost curvature","default":1.2,"bounds":[.1,5],"plausible":[.6,2.5],"stress":[.2,5],"status":"normalized"},
    "beta": {"symbol":"beta","meaning":"discount factor","default":.95,"bounds":[0,1],"plausible":[.8,.98],"stress":[.6,.995],"status":"structural"},
    "misconduct_harm": {"symbol":"L","meaning":"real social harm from misconduct","default":1.2,"bounds":[0,5],"plausible":[.6,2.4],"stress":[0,5],"status":"normalized"},
    "private_benefit_max": {"symbol":"b_max","meaning":"upper misconduct-benefit support","default":1.5,"bounds":[.1,5],"plausible":[1,2.5],"stress":[.2,5],"status":"normalized"},
    "logistic_slope": {"symbol":"k","meaning":"opportunity curvature/slope","default":6,"bounds":[.1,20],"plausible":[3,10],"stress":[.5,20],"status":"normalized"},
    "horizon": {"symbol":"T","meaning":"finite planning horizon","default":6,"bounds":[1,50],"plausible":[4,12],"stress":[2,50],"status":"design"},
}


def validate_registry():
    required={"symbol","meaning","default","bounds","plausible","stress","status"}
    for name,meta in PARAMETER_REGISTRY.items():
        if set(meta)!=required: raise ValueError(f"incomplete metadata: {name}")
        lo,hi=meta["bounds"]
        if not lo <= meta["default"] <= hi: raise ValueError(f"default outside bounds: {name}")
        for range_name in ("plausible","stress"):
            a,b=meta[range_name]
            if not lo <= a <= b <= hi: raise ValueError(f"bad {range_name} range: {name}")
    return True
