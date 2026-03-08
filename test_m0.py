
import sys
import os
from pathlib import Path
import ezdxf
import coffrage_m0_vision_filter

def create_dummy_dxf(path):
    doc = ezdxf.new()
    msp = doc.modelspace()
    # Un "mur"
    msp.add_line((0, 0), (1000, 0))
    msp.add_line((0, 10), (1000, 10))
    # Un "poteau"
    msp.add_lwpolyline([(500, 500), (520, 500), (520, 520), (500, 520)], close=True)
    doc.saveas(str(path))

def test_m0_execution():
    print("Testing M0 execution (fallback mode)...")
    input_dxf = Path("test_input.dxf")
    output_dxf = Path("test_output.dxf")
    audit_dir = Path("test_audit")

    create_dummy_dxf(input_dxf)

    try:
        coffrage_m0_vision_filter.run(
            input_path=input_dxf,
            output_path=output_dxf,
            audit_dir=audit_dir
        )
        print("M0 run completed.")

        assert output_dxf.exists()
        assert (audit_dir / "m0_report.json").exists()
        assert (audit_dir / "m0_raster.png").exists()
        print("Basic output validation passed.")

    finally:
        # Cleanup
        if input_dxf.exists(): input_dxf.unlink()
        if output_dxf.exists(): output_dxf.unlink()
        import shutil
        if audit_dir.exists(): shutil.rmtree(audit_dir)

if __name__ == "__main__":
    test_m0_execution()
